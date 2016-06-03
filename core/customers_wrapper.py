# -*- coding: utf-8 -*-

import sys
from core.customer_provider import CustomerProvider
from core.data_parser import Parser
from core.converter import Converter
from core.spatial_point import SpatialPoint
from core.naive_spatial_search import NaiveSpatialSearch

class CustomersWrapper(object):
    def get_customers_nearby(self, location, radius):
        customers_nearby = []

        customer_provider = CustomerProvider()
        customer_raw_data = customer_provider.get_customer_data()

        parser = Parser()
        customers = parser.parse_customer_spatial_data(customer_raw_data)

        converter = Converter()
        spatial_search = NaiveSpatialSearch(customers, converter.from_degrees_to_radians_point)     

        customers_nearby = spatial_search.search_all_nearby(location, radius)
        customers_nearby.sort()

        return customers_nearby
