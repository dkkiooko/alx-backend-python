#!/usr/bin/env python3
"""create a unittest for a utils function"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """tests accessnestedmap from utils

    Args:
        unittest (_module_): _testing module_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test mapping method """
        self.assertEqual(access_nested_map(nested_map, path), expected)
