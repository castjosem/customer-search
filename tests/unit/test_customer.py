# -*- coding: utf-8 -*-

import core
import unittest

from core.customer import Customer
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest


class CustomerTest(unittest.TestCase):

    @istest
    def it_creates_a_customer(self):
        data = [
            (1, "Ralph")
        ]

        for user_id, name in data:
            customer = Customer(user_id, name)
            eq_(user_id, customer.user_id)
            eq_(name, customer.name)
    

    @istest
    def it_checks_big_user_id(self):
        data = [
            (999999999999999999999999999999999999, "Id")
        ]

        for user_id, name in data:
            customer = Customer(user_id, name)
            eq_(user_id, customer.user_id)
            eq_(name, customer.name)


    @istest
    def it_checks_xbig_user_id(self):
        data = [
            (9999999999999999999999999999999999991111111111111111111111111, "Id")
        ]

        for user_id, name in data:
            customer = Customer(user_id, name)
            eq_(user_id, customer.user_id)
            eq_(name, customer.name)

