# -*- coding: utf-8 -*-

from math import radians

class Converter(object):
    def from_degrees_to_radians_point(self, point):
        return map(radians, [point.latitude, point.longitude])