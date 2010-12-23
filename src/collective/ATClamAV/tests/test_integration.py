import unittest2 as unittest
from StringIO import StringIO
from collective.ATClamAV.testing import EICAR
from collective.ATClamAV.tests import base

class TestIntegration(base.ATClamAVMockFunctionalTestCase):

    def test_atvirusfile(self):
        # Test if a virus-infected file gets caught by the validator
        #self.setRoles('Manager')
        portal = self.layer['portal']
        browser = base.get_browser(self.layer['app'])
        browser.open(portal.absolute_url()+'/virus-folder')
        browser.getLink(url='createObject?type_name=File').click()
        control = browser.getControl(name='file_file')
        control.filename = 'virus.txt'
        control.value = StringIO(EICAR)
        browser.getControl('Save').click()

        self.failIf('Eicar-Test-Signature FOUND' not in browser.contents)

        # And let's see if a clean file passes...
        control = browser.getControl(name='file_file')
        control.filename = 'nonvirus.txt'
        control.value = StringIO('Not a virus')
        browser.getControl('Save').click()
        self.failIf('Changes saved' not in browser.contents)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIntegration))
    return suite
