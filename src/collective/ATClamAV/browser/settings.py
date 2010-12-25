from plone.app.controlpanel.form import ControlPanelForm
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import adapts
from zope.formlib import form
from zope.interface import implements

from collective.ATClamAV import ATClamAVMessageFactory as _
from collective.ATClamAV.interfaces import IAVScannerSettings


class ClamAVControlPanel(ControlPanelForm):

    form_fields = form.FormFields(IAVScannerSettings)

    label = _("ClamAV settings")
    description = _("Clam antivirus host settings.")
    form_name = _("ClamAV settings")


class ClamAVControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(IAVScannerSettings)

    def __init__(self, context):
        super(ClamAVControlPanelAdapter, self).__init__(context)
        properties = getToolByName(context, 'portal_properties')
        self.context = properties.clamav_properties

    # Connection type
    def get_clamav_connection(self):
        return getattr(self.context, 'clamav_connection', "socket")

    def set_clamav_connection(self, value):
        self.context._updateProperty('clamav_connection', value)

    clamav_connection = property(get_clamav_connection, set_clamav_connection)

    # Socket path
    def get_clamav_socket(self):
        return getattr(self.context, 'clamav_socket', '/var/run/clamd')

    def set_clamav_socket(self, value):
        self.context._updateProperty('clamav_socket', value)

    clamav_socket = property(get_clamav_socket, set_clamav_socket)

    # Host
    def get_clamav_host(self):
        return getattr(self.context, 'clamav_host', 'localhost')

    def set_clamav_host(self, value):
        self.context._updateProperty('clamav_host', value)

    clamav_host = property(get_clamav_host, set_clamav_host)

    # Port
    def get_clamav_port(self):
        return int(getattr(self.context, 'clamav_port', '3310'))

    def set_clamav_port(self, value):
        self.context._updateProperty('clamav_port', value)

    clamav_port = property(get_clamav_port, set_clamav_port)

    # Timeout
    def get_clamav_timeout(self):
        return int(getattr(self.context, 'clamav_timeout', '120'))

    def set_clamav_timeout(self, value):
        self.context._updateProperty('clamav_timeout', value)

    clamav_timeout = property(get_clamav_timeout, set_clamav_timeout)
