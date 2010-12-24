from Products.validation import validation
from zope.i18nmessageid import MessageFactory

ATClamAVMessageFactory = MessageFactory('collective.ATClamAV')

from collective.ATClamAV.clamAVValidator import ClamAVValidator
validation.register(ClamAVValidator('isVirusFree'))
