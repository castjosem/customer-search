# -*- coding: utf-8 -*-

class SpatialPoint(object):
    def __init__(self, latitude, longitude, description = None):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.description = description

    def __repr__(self):
        return str(self.__dict__)