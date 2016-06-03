# -*- coding: utf-8 -*-

import core
import unittest

from core.converter import Converter
from core.spatial_point import SpatialPoint
from nose.tools import istest
from nose.tools import eq_

class ConverterTest(unittest.TestCase):

    @istest
    def it_converts_degrees_to_radians(self):
        data = [
            (53.2451022, -6.238335, 0.9293023439508763, -0.10887948559240046),
            (53.1302756, -6.2397222, 0.9272982417120057, -0.10890369679978412),
            (53.1229599, -6.2705202, 0.9271705586599176, -0.10944122330281333),
            (1, 1, 0.017453292519943295, 0.017453292519943295)
        ]

        converter = Converter()
        for latitude, longitude, rad_latitude, rad_longitude in data:
            point = SpatialPoint(latitude, longitude)
            rlat, rlon = converter.from_degrees_to_radians_point(point)
            
            eq_(rlat, rad_latitude)
            eq_(rlon, rad_longitude)

    