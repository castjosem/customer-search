# -*- coding: utf-8 -*-

import json
from core.customer_spatial import CustomerSpatial

class ParseError(Exception):
    pass

class Parser(object):
    def parse_customer_spatial_data(self, customer_raw_data):
        customers = []
        for customer_raw in customer_raw_data:

            try:
                customer_parsed = json.loads(customer_raw)

                user_id = customer_parsed["user_id"]
                name = customer_parsed["name"]
                latitude = customer_parsed["latitude"]
                longitude = customer_parsed["longitude"]

                customer = CustomerSpatial(user_id, name, latitude, longitude)
                customers.append(customer)

            except:
                raise ParseError("error during parsing, invalid or incomplete json")
        return customers