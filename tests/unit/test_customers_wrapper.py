# -*- coding: utf-8 -*-

import core
import unittest

from core.spatial_point import SpatialPoint
from core.customers_wrapper import CustomersWrapper
from nose.tools import istest
from nose.tools import eq_


class CustomersWrapperTest(unittest.TestCase):

    @istest
    def it_gets_customers_nearby_a_specific_place(self):        
        location = SpatialPoint(53.3381985, -6.2592576, "Dublin Office")
        radius = 300
        expected_size = 30

        customers_wrapper = CustomersWrapper()
        nearby = customers_wrapper.get_customers_nearby(location, radius)
        size = len(nearby)
        eq_(size, expected_size)


