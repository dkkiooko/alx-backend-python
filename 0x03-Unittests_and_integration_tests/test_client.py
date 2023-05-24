#!/usr/bin/env python3
""" test module """
import unittest
from unittest import mock
from client import GithubOrgClient
from unittest.mock import (
    MagicMock,
    patch
)
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ tests the `GithubOrgClient` class """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, mock):
        """ test the org method """
        url = 'https://api.github.com/orgs/{}'.format(org)
        spec = GithubOrgClient(org)
        spec.org()
        mock.assert_called_once_with(url)
