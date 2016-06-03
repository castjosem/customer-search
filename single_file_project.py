"""

Let’s say we have some customer records in a text file (customers.txt, see below) – one customer per line, 
JSON-encoded. We want to invite any customer within 100km of our Dublin office (GPS coordinates 53.3381985, -6.2592576) 
for some food and drinks on us.

Write a program that will read the full list of customers and output the names and user ids of matching customers 
(within 100 km), sorted by user id (ascending).


"""

import sys
from math import cos, sin, asin, sqrt, radians


class Converter(object):
    def from_degrees_to_radians_point(self, point):
        return map(radians, [point.latitude, point.longitude])


class SpatialPoint(object):
    def __init__(self, latitude, longitude, description = None):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.description = description

    def __repr__(self):
        return str(self.__dict__)



class SpatialSearch(object):
    def __init__(self, entries, converter = None):
        # Prohibit creating class instance
        if self.__class__ is SpatialSearch:
            raise TypeError('SpatialSearch abstract class cannot be instantiated')

        self.entries = entries
        self.converter = converter

    def search_all_nearby(self, location, radius):
        elem_nearby = self._get__all_nearby(location, radius)
        return elem_nearby


    def _get__all_nearby(self, location, radius):
        raise NotImplementedError()

    def _apply_converter(self, point):
        if self.converter:
            return self.converter(point)
        else:
            return (point.latitude, point.longitude)


    def haversine(self, p1, p2):
        lat1, lon1 = self._apply_converter(p1)
        lat2, lon2 = self._apply_converter(p2)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1 
        
        # Kilometeres
        R = 6367

        a = pow(sin(delta_lat / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(delta_lon / 2), 2)
        c = 2 * asin(sqrt(a)) 
        distance = R * c

        return distance




class NaiveSpatialSearch(SpatialSearch):
    def _get__all_nearby(self, location, radius):
        nearby = []
        for entry in self.entries:
            distance = self.haversine(location, entry)
            if distance < radius:
                nearby.append(entry)
        return nearby

    

class RTreeSpatialSearch(SpatialSearch):
    def _get__all_nearby(self, location, radius):
        pass



class Customer(object):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __lt__(self, other):
        return self.user_id < other.user_id

    def __repr__(self):
        return str(self.__dict__)


class CustomerSpatial(Customer, SpatialPoint):
    def __init__(self, user_id, name, latitude, longitude):
        SpatialPoint.__init__(self, latitude, longitude, "Customer")
        Customer.__init__(self, user_id, name)


import json
class Parser(object):
    def parse_customer_spatial_data(self, customer_raw_data):
        customers = []

        for customer_raw in customer_raw_data:
            customer_parsed = json.loads(customer_raw)

            user_id = customer_parsed["user_id"]
            name = customer_parsed["name"]
            latitude = customer_parsed["latitude"]
            longitude = customer_parsed["longitude"]

            customer = CustomerSpatial(user_id, name, latitude, longitude)
            customers.append(customer)

        return customers


class CustomerProvider(object):
    def __init__(self):
        self.path = 'customers.txt'

    def get_customer_data(self):
        customers_raw = []      
        try:
            with open(self.path, 'r') as file_content:
                customers_raw = file_content.read().splitlines()
        except:
            raise

        return customers_raw



class CustomersWrapper(object):
    def get_customers_nearby(self, location, distance):
        customers_nearby = []

        try:
            customer_provider = CustomerProvider()
            customer_raw_data = customer_provider.get_customer_data()

            parser = Parser()
            customers = parser.parse_customer_spatial_data(customer_raw_data)

            converter = Converter()
            spatial_search = NaiveSpatialSearch(customers, converter.from_degrees_to_radians_point)     

            customers_nearby = spatial_search.search_all_nearby(location, distance)
            customers_nearby.sort()

        except:
            e = sys.exc_info()[0]
            print ( "Error: {}".format(e) )

        return customers_nearby



if __name__ == '__main__':
    dublin_office = SpatialPoint(53.3381985, -6.2592576, "Dublin Office")
    distance = 100

    customers_wrapper = CustomersWrapper()
    customers_wrapper.get_customers_nearby(dublin_office, distance)             


