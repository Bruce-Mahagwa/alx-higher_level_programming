import unittest

from models import base
class Base(unittest.TestCase):
    def test_id_value(self):
        n = Base(10)
        self.assertEqual(print(n.id), 10)
    def test_id_non(self):
        n = Base()
        self.assertEqual(print(n.id), 1)

