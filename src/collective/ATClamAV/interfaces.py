from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary

from collective.ATClamAV import ATClamAVMessageFactory as _

clamdConnectionType = SimpleVocabulary.fromItems((
    (_(u"Local UNIX Socket"), 'socket'),
    (_(u"Network"), 'net')))


class IAVScannerSettings(Interface):
    """ Schema for the ClamAV settings
    """
    clamav_connection = schema.Choice(
        title=_(u"Connection type to clamd"),
        description=_(u"Choose whether clamd is accessible through local "
            "UNIX sockets or network."),
        vocabulary=clamdConnectionType)

    clamav_socket = schema.ASCIILine(
        title=_(u"Clamd local socket file"),
        description=_(u"If connected to clamd through local UNIX sockets, "
            "the path to the local socket file."),
        default = '/var/run/clamd',
        required = True)

    clamav_host = schema.ASCIILine(title=_(u"Scanner host"),
        description=_(u"If connected to clamd through the network, "
            "the host running clamd."),
        default = 'localhost',
        required = True)

    clamav_port = schema.Int(title=_(u"Scanner port"),
        description=_(u"If connected to clamd through the network, "
            "the port on which clamd listens."),
        default=3310,
        required = True)

    clamav_timeout = schema.Int(title=_(u"Timeout"),
        description=_(u"The timeout in seconds for communication with "
            "clamd."),
        default=120,
        required = True)


class IAVScanner(Interface):

    def ping():
        pass

    def scanBuffer(buffer):
        pass
