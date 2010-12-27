from zope.component import getUtility

from collective.ATClamAV.interfaces import IAVScanner
from collective.ATClamAV.scanner import ScanError
from collective.ATClamAV.testing import EICAR
from collective.ATClamAV.tests.base import ATClamAVIntegrationTestCase


class TestScanner(ATClamAVIntegrationTestCase):
    """Integration test for ATClamAV. This testcase communicates with
    clamd, so you need it installed. Provide the -a2 flag to testrunner
    to include it.
    """

    level = 2 # Only run on level 2...

    def setUp(self):
        self.scanner = getUtility(IAVScanner)

    def test_net_ping(self):
        """ Test ping with a network connection on localhost 3310
        """

        self.assertEquals(self.scanner.ping(type='net'), True)

        # Test timeout
        self.assertRaises(
            ScanError,
            self.scanner.ping,
            {'type': 'net', 'timeout': 1.0e-16})

    def test_unix_socket_ping(self):
        """ Test ping with a socket connection on /tmp/clamd.socket
        which is default on macports clamd. If you use linux just change
        the socketpath
        """

        self.assertEquals(
            self.scanner.ping(type='socket', socketpath='/tmp/clamd.socket'),
            True)

        # Test timeout
        self.assertRaises(
            ScanError,
            self.scanner.ping,
            {'type': 'socket',
             'socketpath': '/tmp/clamd.socket',
             'timeout': 1.0e-16})

    def test_net_scanBuffer(self):
        """ Try a virus through the net.
        """

        self.assertEquals(
            self.scanner.scanBuffer(EICAR, type='net'),
            'Eicar-Test-Signature FOUND')

        # And a normal file...
        self.assertEquals(
            self.scanner.scanBuffer('Not a virus', type='net'),
            None)

        # Test timeout
        self.assertRaises(
            ScanError,
            self.scanner.scanBuffer,
            ('Not a virus', ),
            {'type': 'net', 'timeout': 1.0e-16})

    def test_unix_socket_scanBuffer(self):
        """ Try a virus through a unix socket.
        """

        self.assertEquals(
            self.scanner.scanBuffer(
                EICAR, type='socket',
                socketpath='/tmp/clamd.socket'),
            'Eicar-Test-Signature FOUND')

        # And a normal file...
        self.assertEquals(
            self.scanner.scanBuffer('Not a virus', type='socket',
            socketpath='/tmp/clamd.socket'),
            None)

        # Test timeout
        self.assertRaises(
            ScanError,
            self.scanner.scanBuffer,
            ('Not a virus', ),
            {'type': 'socket',
             'socketpath': '/tmp/clamd.socket',
             'timeout': 1.0e-16})
