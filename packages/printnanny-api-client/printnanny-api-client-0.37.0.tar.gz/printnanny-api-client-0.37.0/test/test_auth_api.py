# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.auth_api import AuthApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_verify_create(self):
        """Test case for auth_verify_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
