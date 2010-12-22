from zope.configuration import xmlconfig
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


EICAR = """
    WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5E
    QVJELUFOVElWSVJVUy1URVNU\nLUZJTEUhJEgrSCo=\n""".decode('base64')


class ATClamAVFixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.ATClamAV
        xmlconfig.file('configure.zcml', collective.ATClamAV,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.ATClamAV:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory('Folder', 'virus-folder')
        setRoles(portal, TEST_USER_ID, ['Member'])


ATCLAMAV_FIXTURE = ATClamAVFixture()

ATCLAMAV_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ATCLAMAV_FIXTURE,), name="ATClamAVFixture:Integration")
ATCLAMAV_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ATCLAMAV_FIXTURE,), name="ATClamAVFixture:Functional")
