from zope.i18nmessageid import MessageFactory
from Products.validation import validation
ATClamAVMessageFactory = MessageFactory('collective.ATClamAV')
from collective.ATClamAV.clamAVValidator import ClamAVValidator
validation.register(ClamAVValidator('isVirusFree'))


def initialize(context):
    """
    """
    pass
