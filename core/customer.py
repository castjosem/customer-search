# -*- coding: utf-8 -*-

class Customer(object):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __lt__(self, other):
        return self.user_id < other.user_id

    def __repr__(self):
        return str(self.__dict__)