# -*- coding: utf-8 -*-

import math
import core
import unittest
import random

from core.converter import Converter
from core.spatial_point import SpatialPoint
from core.naive_spatial_search import NaiveSpatialSearch
from nose.tools import istest
from nose.tools import eq_

class NaiveSpatialSearchTest(unittest.TestCase):

    # test data used to generate random points and verify algorithm works
    size = 10

    # 300km
    radius = 300
    location = SpatialPoint(53.3381985, -6.2592576, "Dublin Office")

    @istest
    def it_gets_elements_nearby_location_and_radius(self):
        # generate random points within the test radius
        entry_data = self.generate_random_point_nearby(self.location, self.radius, self.size)

        converter = Converter()
        naive_spatial_search = NaiveSpatialSearch(entry_data, converter.from_degrees_to_radians_point)
        entry_data_nearby = naive_spatial_search._get__all_nearby(self.location, self.radius)
        size_nearby = len(entry_data_nearby)

        # verify all points generated within the radius are obtained from the search
        eq_(size_nearby, self.size)



    def generate_random_point_nearby(self, point, radius, size):
        """ Generates random points near a point given and within the specified radius """

        # transform radius from kilometers to degrees
        radius_in_degrees = (radius * 1000) / 111000
        r = radius_in_degrees

        # store points generated
        generated = []

        for i in range(size):
            u = float(random.uniform(0.0, 1.0))
            v = float(random.uniform(0.0, 1.0))

            w = r * math.sqrt(u)
            t = 2 * math.pi * v
            x = w * math.cos(t) 
            y = w * math.sin(t)

            # new point coordinates
            new_latitude = x + point.latitude
            new_longitude = y + point.longitude

            # add new points to list
            generated.append(SpatialPoint(new_latitude, new_longitude, "Random Point"))

        return generated
