"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.43
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.identity_state import IdentityState
globals()['IdentityState'] = IdentityState
from ory_client.model.admin_update_identity_body import AdminUpdateIdentityBody


class TestAdminUpdateIdentityBody(unittest.TestCase):
    """AdminUpdateIdentityBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdminUpdateIdentityBody(self):
        """Test AdminUpdateIdentityBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AdminUpdateIdentityBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
