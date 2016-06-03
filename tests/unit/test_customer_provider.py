import core
import unittest

from core.customer_provider import CustomerProvider
from nose.tools import istest

class CustomerProviderTest(unittest.TestCase):

    test_path = 'tests/unit/test_customers.txt'

    @istest
    def it_opens_a_file(self):
        customer_provider = CustomerProvider()
        customer_provider.path = self.test_path
        customers = customer_provider.get_customer_data()


    @istest
    def it_opens_a_file_and_reads_content(self):
        customer_provider = CustomerProvider()
        customer_provider.path = self.test_path

        customers = customer_provider.get_customer_data()
        size = len(customers)

        self.assertGreater(size, 0)