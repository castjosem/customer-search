# -*- coding: utf-8 -*-

import core
import unittest

from core.data_parser import Parser
from nose.tools import istest
from nose.tools import eq_

class ParserTest(unittest.TestCase):

    @istest
    def it_parses_raw_data(self):
        data =  [
            '{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}', 
            '{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}', 
            '{"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"}'
        ]

        parser = Parser()
        for raw_data in data:
            customers = parser.parse_customer_spatial_data([raw_data])
            size = len(customers)
            self.assertGreater(size, 0)
