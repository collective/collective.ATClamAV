from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from zope.component import getGlobalSiteManager
from zope.configuration import xmlconfig
from zope.interface import implements

from collective.ATClamAV.interfaces import IAVScanner
from collective.ATClamAV.scanner import ScanError


EICAR = """
    WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5E
    QVJELUFOVElWSVJVUy1URVNU\nLUZJTEUhJEgrSCo=\n""".decode('base64')


class MockAVScanner(object):
    """Mock objects to run tests withoud clamav present.
    """

    implements(IAVScanner)

    def ping(self, type, **kwargs):
        """
        """
        return True

    def scanBuffer(self, buffer, type, **kwargs):
        """
        """
        if EICAR in buffer:
            return 'Eicar-Test-Signature FOUND'
        return None


class AVFixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        import collective.ATClamAV
        xmlconfig.file('configure.zcml', collective.ATClamAV,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.ATClamAV:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Folder', 'virus-folder')
        setRoles(portal, TEST_USER_ID, ['Member'])


AV_FIXTURE = AVFixture()


class AVMockFixture(PloneSandboxLayer):

    defaultBases = (AV_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        gsm = getGlobalSiteManager()
        gsm.registerUtility(MockAVScanner())


AVMOCK_FIXTURE = AVMockFixture()

AV_INTEGRATION_TESTING = IntegrationTesting(
    bases=(AV_FIXTURE, ), name="AVFixture:Integration")
AV_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(AV_FIXTURE, ), name="AVFixture:Functional")
AVMOCK_INTEGRATION_TESTING = IntegrationTesting(
    bases=(AVMOCK_FIXTURE, ), name="AVMockFixture:Integration")
AVMOCK_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(AVMOCK_FIXTURE, ), name="AVMockFixture:Functional")
