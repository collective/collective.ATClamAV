from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_PASSWORD
from plone.testing.z2 import Browser
import unittest2 as unittest

from collective.ATClamAV import testing


def get_browser(app, loggedIn=True):
    browser = Browser(app)
    if loggedIn:
        auth = 'Basic %s:%s' % (TEST_USER_ID, TEST_USER_PASSWORD)
        browser.addHeader('Authorization', auth)
    return browser


class ATClamAVIntegrationTestCase(unittest.TestCase):
    """We use this class for integration tests.
    """
    layer = testing.AV_INTEGRATION_TESTING


class ATClamAVFunctionalTestCase(unittest.TestCase):
    """We use this class for functional tests.
    """
    layer = testing.AV_FUNCTIONAL_TESTING


class ATClamAVMockIntegrationTestCase(unittest.TestCase):
    """We use this class for integration tests.
    """
    layer = testing.AVMOCK_INTEGRATION_TESTING


class ATClamAVMockFunctionalTestCase(unittest.TestCase):
    """We use this class for functional tests.
    """
    layer = testing.AVMOCK_FUNCTIONAL_TESTING
