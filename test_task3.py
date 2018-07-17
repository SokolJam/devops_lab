from unittest.mock import patch
from unittest import TestCase

import task3


class TestPrime(TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        """Test for simple"""
        self.assertFalse(task3.simple(10))
        self.assertTrue(task3.simple(17))
        self.assertEqual(task3.simple(7), 7)

    def test_factor(self):
        self.assertEqual(task3.factor(24), [2, 2, 2, 3])

    @patch('task3.get_input', return_value=15)
    def test_natural(self, value):
        self.assertEqual(task3.natural(), 35)

    @patch('task3.get_input', return_value=15)
    def test_input_value(self, value):
        self.assertEqual(task3.input_value(), 15)

    @patch('task3.get_input', return_value=-1)
    @patch('task3.repeat', return_value='n')
    def test_exit_input_value(self, val1, val2):
        with self.assertRaises(SystemExit):
            task3.input_value()

    def tearDown(self):
        pass
