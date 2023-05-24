#!/usr/bin/env python3
""" test module """
import unittest
from client import GithubOrgClient
from unittest.mock import (
    MagicMock
)
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ tests the `GithubOrgClient` class """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org, resp, mock):
        """ test the org method """
        mock = MagicMock(return_value=resp)
        client = GithubOrgClient(org)
        self.assertEqual(client.org(), resp)
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org}")
