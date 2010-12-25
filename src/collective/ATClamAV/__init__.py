from Products.validation import validation
from zope.i18nmessageid import MessageFactory

ATClamAVMessageFactory = MessageFactory('collective.ATClamAV')

from collective.ATClamAV.validator import ClamAVValidator
validation.register(ClamAVValidator('isVirusFree'))
