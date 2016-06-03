# -*- coding: utf-8 -*-

from core.customer import Customer
from core.spatial_point import SpatialPoint

class CustomerSpatial(Customer, SpatialPoint):
    def __init__(self, user_id, name, latitude, longitude):
        SpatialPoint.__init__(self, latitude, longitude, "Customer")
        Customer.__init__(self, user_id, name)