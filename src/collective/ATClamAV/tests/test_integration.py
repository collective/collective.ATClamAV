import unittest
from StringIO import StringIO
from Products.PloneTestCase.PloneTestCase import default_user
from collective.ATClamAV.tests.base import ATClamAVFunctionalTestCase


class TestIntegration(ATClamAVFunctionalTestCase):

    def test_atvirusfile(self):
        # Test if a virus-infected file gets caught by the validator
        self.setRoles('Manager')
        browser = self.getBrowser()
        browser.open('http://nohost/plone/Members/%s' % default_user)
        browser.getLink(url='createObject?type_name=File').click()
        control = browser.getControl(name='file_file')
        control.filename = 'virus.txt'
        control.value = StringIO(self.EICAR)
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
