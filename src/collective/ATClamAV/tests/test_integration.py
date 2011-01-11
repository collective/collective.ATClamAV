from os.path import dirname, join
from StringIO import StringIO

from collective.ATClamAV.testing import EICAR
from collective.ATClamAV.tests import base
from collective.ATClamAV import tests


def getFileData(filename):
    """ return a file object from the test data folder """
    filename = join(dirname(tests.__file__), 'data', filename)
    return open(filename, 'r').read()


class TestIntegration(base.ATClamAVMockFunctionalTestCase):

    def test_atvirusfile(self):
        # Test if a virus-infected file gets caught by the validator
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
        self.assertTrue('Changes saved' in browser.contents)

    def test_atvirusimage(self):
        # Test if a virus-infected image gets caught by the validator
        image_data = getFileData('image.png')
        portal = self.layer['portal']
        browser = base.get_browser(self.layer['app'])
        browser.open(portal.absolute_url()+'/virus-folder')
        browser.getLink(url='createObject?type_name=Image').click()
        control = browser.getControl(name='image_file')
        control.filename = 'virus.png'
        control.value = StringIO(image_data + EICAR)
        browser.getControl('Save').click()

        self.assertFalse('Changes saved' in browser.contents)
        self.assertTrue('Eicar-Test-Signature FOUND' in browser.contents)

        # And let's see if a clean file passes...
        control = browser.getControl(name='image_file')
        control.filename = 'nonvirus.png'
        control.value = StringIO(image_data)
        browser.getControl('Save').click()
        self.assertTrue('Changes saved' in browser.contents)
