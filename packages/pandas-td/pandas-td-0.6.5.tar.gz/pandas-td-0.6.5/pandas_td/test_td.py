from .td import Connection
from .td import ResultProxy
from .td import StreamingUploader

import collections
import datetime
import gzip
import io
import msgpack
import numpy as np
import pandas as pd

from unittest import TestCase
from nose.tools import eq_, raises

TestDatabase = collections.namedtuple('TestDatabase', ['name', 'count', 'permission', 'created_at', 'updated_at'])
TestTable = collections.namedtuple('TestTable', ['name', 'count', 'estimated_storage_size', 'created_at', 'last_log_timestamp'])

class TestClient(object):
    def databases(self):
        return [
            TestDatabase(
                name = 'test_db',
                count = 0,
                permission = 'administrator',
                created_at = datetime.datetime(2015, 1, 1, 0, 0, 0),
                updated_at = datetime.datetime(2015, 1, 1, 0, 0, 0),
            )
        ]

    def tables(self, database):
        return [
            TestTable(
                name = 'test_tbl',
                count = 0,
                estimated_storage_size = 0,
                created_at = datetime.datetime(2015, 1, 1, 0, 0, 0),
                last_log_timestamp = datetime.datetime(2015, 1, 1, 0, 0, 0),
            )
        ]

class ConnectionTestCase(TestCase):
    def setUp(self):
        self.connection = Connection('test-key', 'test-endpoint')
        self.connection._client = TestClient()

    def test_databases(self):
        d = self.connection.databases()
        eq_(len(d), 1)
        eq_(d.name[0], 'test_db')

    def test_tables(self):
        d = self.connection.tables('test_db')
        eq_(len(d), 1)
        eq_(d.name[0], 'test_tbl')

class ResultProxyTestCase(TestCase):
    pass

class StreamingUploaderTestCase(TestCase):
    def setUp(self):
        client = TestClient()
        self.uploader = StreamingUploader(client, 'test_db', 'test_tbl')

    def test_normalize_time_now(self):
        frame = pd.DataFrame([['a', 1], ['b', 2]], columns=['x', 'y'])
        # time='now'
        f2 = self.uploader.normalize_dataframe(frame, 'now')
        eq_(list(f2.columns), ['x', 'y', 'time'])

    def test_normalize_time_column(self):
        frame = pd.DataFrame([[0, 'a', 1], [0, 'b', 2]], columns=['time', 'x', 'y'])
        # time='column'
        f1 = self.uploader.normalize_dataframe(frame, 'column')
        eq_(list(f1.columns), ['time', 'x', 'y'])

    def test_normalize_time_index(self):
        date_range = pd.date_range('2015-01-01', periods=2, freq='d')
        frame = pd.DataFrame([['a', 1], ['b', 2]], columns=['x', 'y'], index=date_range)
        # time='index'
        f1 = self.uploader.normalize_dataframe(frame, 'index')
        eq_(list(f1.columns), ['x', 'y', 'time'])

    @raises(ValueError)
    def test_raise_invalid_time(self):
        frame = pd.DataFrame([['a', 1], ['b', 2]], columns=['x', 'y'])
        self.uploader.normalize_dataframe(frame, 'invalid')

    def test_chunk_frame(self):
        frame = pd.DataFrame([[1], [2], [3], [4]])
        chunks = [chunk for chunk in self.uploader._chunk_frame(frame, 2)]
        eq_(len(chunks), 2)

    def test_pack(self):
        records = [{'x': 'a', 'y': 1}, {'x': 'b', 'y': 2}]
        data = self.uploader._pack(pd.DataFrame(records))
        for unpacked in msgpack.Unpacker(io.BytesIO(data), encoding='utf-8'):
            eq_(unpacked, records[0])
            records = records[1:]
        eq_(records, [])

    def test_gzip(self):
        data = self.uploader._gzip(b'abc')
        with gzip.GzipFile(fileobj=io.BytesIO(data)) as f:
            eq_(f.read(), b'abc')
