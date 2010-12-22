from zope.i18nmessageid import MessageFactory
from Products.validation import validation
ATClamAVMessageFactory = MessageFactory('collective.ATClamAV')
# Force validator registration now, before anything else.
# Otherwise something gets screwed, and the validator is not registered.
from collective.ATClamAV.clamAVValidator import ClamAVValidator
validation.register(ClamAVValidator('isVirusFree'))


def initialize(context):
    """
    """
    pass
