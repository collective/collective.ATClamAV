import unittest
from zope.component import getUtility

from collective.ATClamAV.interfaces import IAVScanner
from collective.ATClamAV.tests.base import ATClamAVTestCase


class TestScanner(ATClamAVTestCase):
    """
    """

    def afterSetUp(self):
        self.scanner = getUtility(IAVScanner)

    def test_ping(self):
        """
        """
        # Test ping with a network connection on localhost 3310
        self.assertEquals(self.scanner.ping(type='net'), True)

        # Test ping with a socket connection on /tmp/clamd.socket
        # which is default on macports clamd. If you use linux just change
        # the socketpath

        self.assertEquals(
            self.scanner.ping(type='socket', socketpath='/tmp/clamd.socket'),
            True)

    def test_scanBuffer(self):
        """
        """
        # Try a virus through the net...
        self.assertEquals(
            self.scanner.scanBuffer(self.EICAR, type='net'),
            'Eicar-Test-Signature FOUND')

        # Try a virus through sockets...
        self.assertEquals(
            self.scanner.scanBuffer(
                self.EICAR, type='socket',
                socketpath='/tmp/clamd.socket'),
            'Eicar-Test-Signature FOUND')

        # And a normal file...
        self.assertEquals(
            self.scanner.scanBuffer('Not a virus', type='net'),
            None)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestScanner))
    return suite
