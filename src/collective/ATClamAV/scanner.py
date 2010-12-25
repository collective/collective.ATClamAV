import socket

from zope.interface import implements

from collective.ATClamAV.interfaces import IAVScanner


class ScanError(Exception):
    """Generic exception for AV checks.
    """

    def __init__(self, message):
        super(ScanError, self).__init__(message)


class ClamAVScanner(object):
    """
    """
    implements(IAVScanner)

    def ping(self, type, **kwargs):
        s = None
        timeout = kwargs.get('timeout', 10.0)
        if type=='socket':
            socketpath = kwargs.get('socketpath', '/var/run/clamd')
            s = self._init_unix_socket(filename=socketpath, timeout=timeout)
            host = 'localhost'
        elif type=='net':
            host = kwargs.get('host', 'localhost')
            port = kwargs.get('port', 3310)
            s = self._init_network_socket(host=host, port=port,
                                          timeout=timeout)
        else:
            raise ScanError('Invalid call to ping')

        try:
            s.send('PING')
            result = s.recv(20000)
            s.close()
        except socket.error:
            raise ScanError('Could not ping clamd server')

        if result=='PONG\n':
            return True
        else:
            raise ScanError('Could not ping clamd server')

    def scanBuffer(self, buffer, type, **kwargs):
        """Scans a buffer for viruses
        """

        s = None
        timeout = kwargs.get('timeout', 120.0)

        if type=='socket':
            socketpath = kwargs.get('socketpath', '/var/run/clamd')
            s = self._init_unix_socket(filename=socketpath, timeout=timeout)
            host = 'localhost'
        elif type=='net':
            host = kwargs.get('host', 'localhost')
            port = kwargs.get('port', 3310)
            s = self._init_network_socket(host=host, port=port,
                                          timeout=timeout)
        else:
            raise ScanError('Invalid call to scanBuffer')

        try:
            s.send('STREAM')
            sport = int(s.recv(200).strip().split(' ')[1])
        except socket.error:
            s.close()
            raise ScanError('Error communicating with clamd')

        n = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        n.settimeout(timeout)

        try:
            n.connect((host, sport))
            sended = n.send(buffer)
        except socket.error:
            s.close()
            raise ScanError('Error communicating with clamd')
        finally:
            n.close()

        if sended<len(buffer):
            raise ScanError('BufferTooLong')

        result='...'
        try:
            while result!='':
                result = s.recv(20000)
                if len(result)>0:
                    virusname = result.strip().split(':')[1].strip()
                    if virusname[-5:]=='ERROR':
                        raise ScanError(virusname)
        except socket.error:
            raise ScanError('Error communicating with clamd')
        finally:
            s.close()

        if virusname == 'OK':
            return None
        else:
            return virusname

    def _init_unix_socket(self, filename="/var/run/clamd", timeout=120.0):
        """Initialize scanner to use clamd unix local socket
        """

        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect(filename)
        except socket.error:
            raise ScanError('Could not reach clamd using unix socket (%s)' % \
                            filename)
        return s

    def _init_network_socket(self, host="localhost", port=3310,
                                timeout=120.0):
        """Initialize scanner to use clamd network socket
        """

        try:
            s = socket.create_connection((host, port), timeout=timeout)
        except socket.error:
            raise ScanError('Could not reach clamd on network (%s:%s)' % \
                            (host, port))
        return s
