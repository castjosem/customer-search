# -*- coding: utf-8 -*-

from math import cos, sin, asin, sqrt
from core.converter import Converter
from core.spatial_point import SpatialPoint


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