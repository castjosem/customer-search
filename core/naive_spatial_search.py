# -*- coding: utf-8 -*-

from core.spatial_search import SpatialSearch

class NaiveSpatialSearch(SpatialSearch):
    def _get__all_nearby(self, location, radius):
        nearby = []
        for entry in self.entries:
            distance = self.haversine(location, entry)
            if distance < radius:
                nearby.append(entry)
        return nearby
