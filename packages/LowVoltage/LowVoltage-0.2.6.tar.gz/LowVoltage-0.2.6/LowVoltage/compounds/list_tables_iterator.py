# coding: utf8

# Copyright 2014-2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest

import MockMockMock

import LowVoltage as _lv
import LowVoltage.testing as _tst
from .iterator import Iterator


class ListTablesIterator(Iterator):
    """Make as many "ListTables" actions as needed to iterate over all tables."""

    def __init__(self, connection):
        Iterator.__init__(self, connection, _lv.ListTables())

    def process(self, action, r):
        if r.last_evaluated_table_name is None:
            action = None
        else:
            action.exclusive_start_table_name(r.last_evaluated_table_name)
        return action, r.table_names


class ListTablesIteratorUnitTests(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.connection = self.mocks.create("connection")
        super(ListTablesIteratorUnitTests, self).setUp()

    def tearDown(self):
        self.mocks.tearDown()
        super(ListTablesIteratorUnitTests, self).tearDown()

    class Checker(object):
        def __init__(self, expected_payload):
            self.__expected_payload = expected_payload

        def __call__(self, args, kwds):
            assert len(args) == 1
            assert len(kwds) == 0
            action, = args
            return action.name == "ListTables" and action.build() == self.__expected_payload

    def test_no_tables(self):
        self.connection.expect.request.withArguments(self.Checker({})).andReturn(_lv.ListTables.Result(TableNames=[]))

        self.assertEqual(
            list(ListTablesIterator(self.connection.object)),
            []
        )

    def test_one_page(self):
        self.connection.expect.request.withArguments(self.Checker({})).andReturn(_lv.ListTables.Result(TableNames=["A", "B", "C"]))

        self.assertEqual(
            list(ListTablesIterator(self.connection.object)),
            ["A", "B", "C"]
        )

    def test_one_page_followed_by_empty_page(self):
        self.connection.expect.request.withArguments(self.Checker({})).andReturn(_lv.ListTables.Result(TableNames=["A", "B", "C"], LastEvaluatedTableName="D"))
        self.connection.expect.request.withArguments(self.Checker({"ExclusiveStartTableName": "D"})).andReturn(_lv.ListTables.Result(TableNames=[]))

        self.assertEqual(
            list(ListTablesIterator(self.connection.object)),
            ["A", "B", "C"]
        )

    def test_several_pages(self):
        self.connection.expect.request.withArguments(self.Checker({})).andReturn(_lv.ListTables.Result(TableNames=["A", "B", "C"], LastEvaluatedTableName="D"))
        self.connection.expect.request.withArguments(self.Checker({"ExclusiveStartTableName": "D"})).andReturn(_lv.ListTables.Result(TableNames=["E", "F", "G"], LastEvaluatedTableName="H"))
        self.connection.expect.request.withArguments(self.Checker({"ExclusiveStartTableName": "H"})).andReturn(_lv.ListTables.Result(TableNames=["I", "J", "K"]))

        self.assertEqual(
            list(ListTablesIterator(self.connection.object)),
            ["A", "B", "C", "E", "F", "G", "I", "J", "K"]
        )


class ListTablesIteratorLocalIntegTests(_tst.LocalIntegTests):
    table_names = ["Tab{:03}".format(i) for i in range(103)]

    def setUp(self):
        super(ListTablesIteratorLocalIntegTests, self).setUp()
        for t in self.table_names:
            self.connection.request(
                _lv.CreateTable(t).hash_key("h", _lv.STRING).provisioned_throughput(1, 1)
            )

    def tearDown(self):
        for t in self.table_names:
            self.connection.request(_lv.DeleteTable(t))
        super(ListTablesIteratorLocalIntegTests, self).tearDown()

    def test(self):
        self.assertEqual(
            list(_lv.ListTablesIterator(self.connection)),
            self.table_names
        )
