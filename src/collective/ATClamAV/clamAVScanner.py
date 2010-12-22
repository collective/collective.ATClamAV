from collective.ATClamAV.interfaces import IAVScanner
from zope.interface import implements
import socket


class ClamAVScanner(object):
    """
    """
    implements(IAVScanner)

    def ping(self, type, **kwargs):
        """
        """

        s = None
        if type=='socket':
            socketpath = kwargs.get('socketpath', '/var/run/clamd')
            s = self.__init_unix_socket__(socketpath)
            host = 'localhost'
        elif type=='net':
            host = kwargs.get('host', 'localhost')
            port = kwargs.get('port', 3310)
            s = self.__init_network_socket__(host, port)
        else:
            raise 'ScanError', 'Invalid call to ping'

        try:
            s.send('PING')
            result = s.recv(20000)
            s.close()
        except:
            raise 'ScanError', 'Could not ping clamd server'

        if result=='PONG\n':
            return True
        else:
            raise 'ScanError', 'Could not ping clamd server'

    def scanBuffer(self, buffer, type, **kwargs):
        """Scans a buffer for viruses
        """

        s = None
        if type=='socket':
            socketpath = kwargs.get('socketpath', '/var/run/clamd')
            s = self.__init_unix_socket__(socketpath)
            host = 'localhost'
        elif type=='net':
            host = kwargs.get('host', 'localhost')
            port = kwargs.get('port', 3310)
            s = self.__init_network_socket__(host, port)
        else:
            raise 'ScanError', 'Invalid call to scanBuffer'

        s.send('STREAM')
        sport = int(s.recv(200).strip().split(' ')[1])
        n=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        n.connect((host, sport))

        sended = n.send(buffer)
        n.close()

        if sended<len(buffer):
            raise 'BufferTooLong'

        result='...'
        while result!='':
            result = s.recv(20000)
            if len(result)>0:
                virusname = result.strip().split(':')[1].strip()
                if virusname[-5:]=='ERROR':
                    raise 'ScanError', virusname
        s.close()
        if virusname=='OK':
            return None
        else:
            return virusname

    def __init_unix_socket__(self, filename="/var/run/clamd"):
        """Initialize scanner to use clamd unix local socket
        """

        s=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            s.connect(filename)
        except socket.error:
            raise 'ScanError', 'Could not reach clamd'\
            ' using unix socket (%s)'%filename
        return s

    def __init_network_socket__(self, host, port):
        """Initialize scanner to use clamd network socket
        """

        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
        except socket.error:
            raise 'ScanError', 'Could not reach clamd' \
            ' on network (%s:%s)' % (host, port)
        return s
