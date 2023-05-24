#!/usr/bin/env python3
"""create a unittest for a utils function"""
import requests
import unittest
from parameterized import parameterized
from utils import (access_nested_map, get_json)
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ test key error is raised """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """ mock HTTP calls """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test utils.get_json """
        attr = {'json.return_value': test_payload}
        patcher = patch('requests.get', return_value=Mock(**attr))
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
