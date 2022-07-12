#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_instantiation(self):
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        instance4 = Base(None)
        instance5 = Base(250)
        instance6 = Base()

        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)
        self.assertEqual(instance4.id, 4)
        self.assertEqual(instance5.id, 250)
        self.assertEqual(instance6.id, 5)
