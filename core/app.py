# -*- coding: utf-8 -*-


from customers_wrapper import CustomersWrapper
from spatial_point import SpatialPoint




if __name__ == '__main__':

    dublin_office = SpatialPoint(53.3381985, -6.2592576, "Dublin Office")
    radius = 100

    customers_wrapper = CustomersWrapper()
    customers_nearby = customers_wrapper.get_customers_nearby(dublin_office, radius)

    for customer in customers_nearby:
        print ("Name: {name:20} Id: {user_id}".format(name = customer.name, user_id = customer.user_id))