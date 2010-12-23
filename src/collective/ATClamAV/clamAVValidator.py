from zope.interface import implements
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot
from Products.validation.interfaces.IValidator import IValidator
from collective.ATClamAV.interfaces import IAVScanner
from collective.ATClamAV.clamAVScanner import ScanError


class ClamAVValidator:

    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        if hasattr(value, 'seek'):
            # when submitted a new file 'value' is a
            # 'ZPublisher.HTTPRequest.FileUpload'

            siteroot = getUtility(ISiteRoot)
            settings = siteroot.portal_properties.clamav_properties
            scanner = getUtility(IAVScanner)

            value.seek(0)
            content = value.read()
            result = ''
            try:
                if settings.clamav_connection == 'net':
                    result = scanner.scanBuffer(
                        content, 'net',
                        host=settings.clamav_host,
                        port=int(settings.clamav_port),
                        timeout=float(settings.clamav_timeout))
                else:
                    result = scanner.scanBuffer(content, 'socket',
                        socketpath=settings.clamav_socket,
                        timeout=float(settings.clamav_timeout))
            except ScanError:
                return "There was an error while checking the file " \
                "for viruses: Please contact your system administrator."

            if result:
                return "Validation failed, file is virus-infected. (%s)" % \
                    (result)
            else:
                return 1
        else:
            # if we keeped existing file
            return 1
