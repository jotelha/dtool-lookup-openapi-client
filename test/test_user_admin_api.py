"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import dtool-lookup-openapi-client
from dtool_lookup_openapi_client.user_admin_api import UserAdminApi  # noqa: E501


class TestUserAdminApi(unittest.TestCase):
    """UserAdminApi unit test stubs"""

    def setUp(self):
        self.api = UserAdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_user_list_get(self):
        """Test case for admin_user_list_get

        List the users in the dtool lookup server.  # noqa: E501
        """
        pass

    def test_admin_user_register_post(self):
        """Test case for admin_user_register_post

        Register a user in the dtool lookup server.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
