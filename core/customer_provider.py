# -*- coding: utf-8 -*-

class CustomerProvider(object):
    def __init__(self):
        self.path = 'customers.txt'

    def get_customer_data(self):
        customers_raw = []      
        try:
            with open(self.path, 'r') as file_content:
                customers_raw = file_content.read().splitlines()
        except:
            raise

        return customers_raw