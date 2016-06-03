# -*- coding: utf-8 -*-

import core
import unittest

from core.spatial_point import SpatialPoint
from nose.tools import istest
from nose.tools import eq_

class SpatialPointTest(unittest.TestCase):

    @istest
    def it_creates_a_spatial_point(self):
        data = [
            (53.2451022, -6.238335, "Spatial Point")
        ]

        for latitude, longitude, description in data:
            point = SpatialPoint(latitude, longitude, description)

            eq_(latitude, point.latitude)
            eq_(longitude, point.longitude)
            eq_(description, point.description)