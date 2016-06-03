# -*- coding: utf-8 -*-

import core
import unittest

from core.customer_spatial import CustomerSpatial
from core.customer import Customer
from nose.tools import istest
from nose.tools import eq_

class CustomerSpatialTest(unittest.TestCase):

    @istest
    def it_creates_a_customer_spatial(self):
        data = [
            (1, "Ralph", 53.2451022, -6.238335)
        ]

        for user_id, name, latitude, longitude in data:
            customer = CustomerSpatial(user_id, name, latitude, longitude)

            eq_(user_id, customer.user_id)
            eq_(name, customer.name)
            eq_(latitude, customer.latitude)
            eq_(longitude, customer.longitude)