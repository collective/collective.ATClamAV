import logging

import Globals
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.utils import getToolByName
from Products.validation.interfaces.IValidator import IValidator
from zope.component import getUtility
from zope.interface import implements

from collective.ATClamAV.interfaces import IAVScanner
from collective.ATClamAV.scanner import ScanError

logger = logging.getLogger('collective.ATClamAV')


class ClamAVValidator:

    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        if Globals.DevelopmentMode: # pragma: no cover
            logger.warn('Skipping virus scan in development mode.')
            return True

        if hasattr(value, 'seek'):
            # when submitted a new file 'value' is a
            # 'ZPublisher.HTTPRequest.FileUpload'

            if getattr(value, '_validate_isVirusFree', False):
                # validation is called multiple times for the same file upload
                return True

            siteroot = getUtility(ISiteRoot)
            ptool = getToolByName(siteroot, 'portal_properties')
            settings = ptool.clamav_properties
            scanner = getUtility(IAVScanner)

            value.seek(0)
            # TODO this reads the entire file into memory, there should be
            # a smarter way to do this
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
            except ScanError as e:
                logger.error('ScanError %s on %s.' % (e, value.filename))
                return "There was an error while checking the file for " \
                    "viruses: Please contact your system administrator."

            if result:
                return "Validation failed, file is virus-infected. (%s)" % \
                    (result)
            else:
                # mark the file upload instance as already checked
                value._validate_isVirusFree = True
                return True
        else:
            # if we kept existing file
            return True
