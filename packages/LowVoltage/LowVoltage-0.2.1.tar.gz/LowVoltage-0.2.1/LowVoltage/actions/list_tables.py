# coding: utf8

# Copyright 2014-2015 Vincent Jacques <vincent@vincent-jacques.net>

import unittest

import LowVoltage as _lv
import LowVoltage.testing as _tst
from .action import Action
from .return_types import _is_str, _is_list_of_str


class ListTables(Action):
    """http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html#API_ListTables_RequestParameters"""

    class Result(object):
        """http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html#API_ListTables_ResponseElements"""

        def __init__(
            self,
            LastEvaluatedTableName=None,
            TableNames=None,
            **dummy
        ):
            self.last_evaluated_table_name = None
            if _is_str(LastEvaluatedTableName):  # pragma no branch (Defensive code)
                self.last_evaluated_table_name = LastEvaluatedTableName

            self.table_names = None
            if _is_list_of_str(TableNames):  # pragma no branch (Defensive code)
                self.table_names = TableNames

    def __init__(self):
        super(ListTables, self).__init__("ListTables")
        self.__limit = None
        self.__exclusive_start_table_name = None

    def build(self):
        data = {}
        if self.__limit:
            data["Limit"] = str(self.__limit)
        if self.__exclusive_start_table_name:
            data["ExclusiveStartTableName"] = self.__exclusive_start_table_name
        return data

    def limit(self, limit):
        self.__limit = limit
        return self

    def exclusive_start_table_name(self, table_name):
        self.__exclusive_start_table_name = table_name
        return self


class ListTablesUnitTests(unittest.TestCase):
    def testName(self):
        self.assertEqual(ListTables().name, "ListTables")

    def testNoArguments(self):
        self.assertEqual(ListTables().build(), {})

    def testLimit(self):
        self.assertEqual(ListTables().limit(42).build(), {"Limit": "42"})

    def testExclusiveStartTableName(self):
        self.assertEqual(ListTables().exclusive_start_table_name("Bar").build(), {"ExclusiveStartTableName": "Bar"})


class ListTablesLocalIntegTests(_tst.LocalIntegTests):
    def setUp(self):
        super(ListTablesLocalIntegTests, self).setUp()
        self.connection.request(
            _lv.CreateTable("Aaa").hash_key("h", _lv.STRING).provisioned_throughput(1, 2)
        )
        self.connection.request(
            _lv.CreateTable("Bbb").hash_key("h", _lv.STRING).provisioned_throughput(1, 2)
        )
        self.connection.request(
            _lv.CreateTable("Ccc").hash_key("h", _lv.STRING).provisioned_throughput(1, 2)
        )

    def tearDown(self):
        self.connection.request(_lv.DeleteTable("Aaa"))
        self.connection.request(_lv.DeleteTable("Bbb"))
        self.connection.request(_lv.DeleteTable("Ccc"))
        super(ListTablesLocalIntegTests, self).tearDown()

    def testAllArguments(self):
        r = self.connection.request(_lv.ListTables().exclusive_start_table_name("Aaa").limit(1))

        with _tst.cover("r", r) as r:
            self.assertEqual(r.last_evaluated_table_name, "Bbb")
            self.assertEqual(r.table_names[0], "Bbb")

    def testNoArguments(self):
        r = self.connection.request(_lv.ListTables())

        with _tst.cover("r", r) as r:
            self.assertEqual(r.last_evaluated_table_name, None)
            self.assertEqual(r.table_names[0], "Aaa")
            self.assertEqual(r.table_names[1], "Bbb")
            self.assertEqual(r.table_names[2], "Ccc")
