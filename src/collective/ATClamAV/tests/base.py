from Products.PloneTestCase import PloneTestCase
from Products.Five.testbrowser import Browser
from collective.ATClamAV.tests.layer import ATClamAVLayer

PloneTestCase.setupPloneSite()


class ATClamAVTestCase(PloneTestCase.PloneTestCase):
    """We use this base class for all the tests in this package.
    """
    layer = ATClamAVLayer
    EICAR = 'WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5E'.decode('base64') \
        +'QVJELUFOVElWSVJVUy1URVNU\nLUZJTEUhJEgrSCo=\n'.decode('base64')


class ATClamAVFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """We use this class for functional integration tests.
    """
    layer = ATClamAVLayer
    EICAR = 'WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5E'.decode('base64') \
        +'QVJELUFOVElWSVJVUy1URVNU\nLUZJTEUhJEgrSCo=\n'.decode('base64')

    def getCredentials(self):
        return '%s:%s' % (PloneTestCase.default_user,
            PloneTestCase.default_password)

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = Browser()
        if loggedIn:
            auth = 'Basic %s' % self.getCredentials()
            browser.addHeader('Authorization', auth)
        return browser
