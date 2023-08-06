import contextlib
import gzip
import io
import os
import time
import uuid
import zlib

import msgpack
import numpy as np
import pandas as pd
import requests
import tdclient

import logging
logger = logging.getLogger(__name__)

DEFAULT_ENDPOINT = 'https://api.treasuredata.com/'

class Connection(object):
    def __init__(self, apikey=None, endpoint=None, **kwargs):
        if apikey is None:
            apikey = os.environ['TD_API_KEY']
        if endpoint is None:
            endpoint = DEFAULT_ENDPOINT
        if not endpoint.endswith('/'):
            endpoint = endpoint + '/'
        self.apikey = apikey
        self.endpoint = endpoint
        self._kwargs = kwargs

    @property
    def client(self):
        if not hasattr(self, '_client'):
            self._client = tdclient.Client(self.apikey, self.endpoint, **self._kwargs)
        return self._client

    def databases(self):
        databases = self.client.databases()
        if databases:
            return pd.DataFrame(
                [[db.name, db.count, db.permission, db.created_at, db.updated_at] for db in databases],
                columns=['name', 'count', 'permission', 'created_at', 'updated_at'])
        else:
            return pd.DataFrame()

    def tables(self, database):
        tables = self.client.tables(database)
        if tables:
            return pd.DataFrame(
                [[t.name, t.count, t.estimated_storage_size, t.last_log_timestamp, t.created_at] for t in tables],
                columns=['name', 'count', 'estimated_storage_size', 'last_log_timestamp', 'created_at'])
        else:
            return pd.DataFrame()

    def query_engine(self, database, **kwargs):
        return QueryEngine(self, database, **kwargs)

class QueryEngine(object):
    def __init__(self, connection, database, **kwargs):
        self.connection = connection
        self.database = database
        self._kwargs = kwargs

    def execute(self, query, **kwargs):
        # parameters
        params = self._kwargs.copy()
        params.update(kwargs)

        # issue query
        job = self.connection.client.query(self.database, query, **params)
        while not job.finished():
            time.sleep(2)
            job._update_status()

        # status check
        if not job.success():
            stderr = job._debug['stderr']
            if stderr:
                logger.error(stderr)
            raise RuntimeError("job {0} {1}\n\nOutput:\n{2}".format(
                job.job_id,
                job.status(),
                job._debug['cmdout']))

        # result
        return ResultProxy(self, job)

class ResultProxy(object):
    def __init__(self, engine, job):
        self.engine = engine
        self.job = job
        self._iter = None

    @property
    def status(self):
        return self.job.status()

    @property
    def size(self):
        return self.job._result_size

    @property
    def description(self):
        return self.job._hive_result_schema

    def iter_content(self, chunk_size):
        # start downloading
        headers = {
            'Authorization': 'TD1 {0}'.format(self.engine.connection.apikey),
            'Accept-Encoding': 'deflate, gzip',
        }
        r = requests.get('{endpoint}v3/job/result/{job_id}?format={format}'.format(
            endpoint = self.engine.connection.endpoint,
            job_id = self.job.job_id,
            format = 'msgpack.gz',
        ), headers=headers, stream=True)

        # content length
        maxval = None
        if 'Content-length' in r.headers:
            maxval = int(r.headers['Content-length'])

        # download
        with contextlib.closing(r) as r:
            d = zlib.decompressobj(16+zlib.MAX_WBITS)
            for chunk in r.iter_content(chunk_size):
                yield d.decompress(chunk)

    def read(self, size=16384):
        if self._iter is None:
            self._iter = self.iter_content(size)
        try:
            return next(self._iter)
        except StopIteration:
            return ''

    def __iter__(self):
        for record in msgpack.Unpacker(self, encoding='utf-8'):
            yield record

    def to_dataframe(self):
        columns = [c[0] for c in self.description]
        return pd.DataFrame(iter(self), columns=columns)

class StreamingUploader(object):
    def __init__(self, client, database, table):
        self.client = client
        self.database = database
        self.table = table

    def current_time(self):
        return int(time.time())

    def normalize_dataframe(self, frame, time, index):
        # time column
        if time != 'column' and 'time' in frame.columns:
            logger.warning('"time" column is overwritten.  Use time="column" to preserve "time" column')
        if time == 'column':
            if 'time' not in frame.columns:
                raise TypeError('"time" column is required when time="column"')
            if frame.time.dtype not in (np.dtype('int64'), np.dtype('datetime64[ns]')):
                raise TypeError('time type must be either int64 or datetime64')
            if frame.time.dtype == np.dtype('datetime64[ns]'):
                frame = frame.copy()
                frame['time'] = frame.time.astype(np.int64, copy=True) // 10 ** 9
        elif time == 'now':
            frame = frame.copy()
            frame['time'] = self.current_time()
        elif time == 'index':
            if frame.index.dtype != np.dtype('datetime64[ns]'):
                raise TypeError('index type must be datetime64[ns]')
            frame = frame.copy()
            frame['time'] = frame.index.astype(np.int64) // 10 ** 9
            index = False
        else:
            raise ValueError('invalid value for time', time)
        # index column
        if index:
            if 'id' in frame.columns:
                logger.warning('"id" column is overwritten. Consider using index=False or rename it')
            frame['id'] = frame.index
        return frame

    def chunk_frame(self, frame, chunksize):
        records = []
        record_count = 0
        for _, row in frame.iterrows():
            record = dict(row)
            records.append(record)
            record_count += 1
            if chunksize is not None and record_count >= chunksize:
                yield records
                records = []
                record_count = 0
        if record_count > 0:
            yield records

    def pack_gz(self, records):
        buff = io.BytesIO()
        with gzip.GzipFile(fileobj=buff, mode='wb') as f:
            for record in records:
                f.write(msgpack.packb(record))
        return buff.getvalue()

    def upload(self, data):
        database = self.database
        table = self.table
        data_size = len(data)
        unique_id = uuid.uuid4()
        elapsed = self.client.import_data(database, table, 'msgpack.gz', data, data_size, unique_id)
        logger.debug('imported %d bytes in %.3f secs', data_size, elapsed)

# utility functions

def connect(apikey=None, endpoint=None, **kwargs):
    return Connection(apikey, endpoint, **kwargs)

def read_td_query(query, engine, **kwargs):
    '''Read Treasure Data table into a DataFrame.

    This method converts the dataframe into a series of key-value pairs
    and send them using the Treasure Data streaming API. The data is divided
    into chunks of rows (default 10,000) and uploaded separately. If upload
    failed, the client retries the process for a certain amount of time
    (max_cumul_retry_delay; default 600 secs). This method may fail and
    raise an exception when retries did not success, in which case the data
    may be partially inserted. Use the bulk import utility if you cannot
    accept partial inserts.

    Parameters
    ----------
    frame : DataFrame
        DataFrame to be written.
    name : string
        Name of table to be written, in the form 'database.table'.
    con : Connection
        Connection to a Treasure Data account.
    if_exists: {'fail', 'replace', 'append'}, default 'fail'
        - fail: If table exists, do nothing.
        - replace: If table exists, drop it, recreate it, and insert data.
        - append: If table exists, insert data. Create if does not exist.
    time : {'now', 'column', 'index'}, default 'now'
        - now: Insert (or replace) a "time" column as the current time.
        - column: Use "time" column in the dataframe.
        - index: Convert DataFrame index into a "time" column. This implys index=False.
    index : boolean, default True
        Write DataFrame index as a column.
    chunksize : int, default 10,000
        Number of rows to be inserted in each chunk from the dataframe.
    '''
    r = engine.execute(query, **kwargs)
    return r.to_dataframe()

# read_td is an alias of read_td_query
read_td = read_td_query

def to_td(frame, name, con, if_exists='fail', time='now', index=True, chunksize=10000):
    '''Write a DataFrame to a Treasure Data table.

    This method converts the dataframe into a series of key-value pairs
    and send them using the Treasure Data streaming API. The data is divided
    into chunks of rows (default 10,000) and uploaded separately. If upload
    failed, the client retries the process for a certain amount of time
    (max_cumul_retry_delay; default 600 secs). This method may fail and
    raise an exception when retries did not success, in which case the data
    may be partially inserted. Use the bulk import utility if you cannot
    accept partial inserts.

    Parameters
    ----------
    frame : DataFrame
        DataFrame to be written.
    name : string
        Name of table to be written, in the form 'database.table'.
    con : Connection
        Connection to a Treasure Data account.
    if_exists: {'fail', 'replace', 'append'}, default 'fail'
        - fail: If table exists, do nothing.
        - replace: If table exists, drop it, recreate it, and insert data.
        - append: If table exists, insert data. Create if does not exist.
    time : {'now', 'column', 'index'}, default 'now'
        - now: Insert (or replace) a "time" column as the current time.
        - column: Use "time" column in the dataframe.
        - index: Convert DataFrame index into a "time" column. This implys index=False.
    index : boolean, default True
        Write DataFrame index as a column.
    chunksize : int, default 10,000
        Number of rows to be inserted in each chunk from the dataframe.
    '''
    database, table = name.split('.')

    # check existence
    if if_exists == 'fail':
        try:
            con.client.table(database, table)
        except tdclient.api.NotFoundError:
            con.client.create_log_table(database, table)
        else:
            raise RuntimeError('table "%s" already exists' % name)
    elif if_exists == 'replace':
        try:
            t = con.client.table(database, table)
        except tdclient.api.NotFoundError:
            pass
        else:
            t.delete()
        con.client.create_log_table(database, table)
    elif if_exists == 'append':
        try:
            con.client.table(database, table)
        except tdclient.api.NotFoundError:
            con.client.create_log_table(database, table)
    else:
        raise ValueError('invalid value for if_exists: %s' % if_exists)

    # upload
    uploader = StreamingUploader(con.client, database, table)
    frame = uploader.normalize_dataframe(frame, time, index)
    for records in uploader.chunk_frame(frame, chunksize):
        uploader.upload(uploader.pack_gz(records))
