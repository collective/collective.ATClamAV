from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from plone.app.blob.subtypes.file import ExtensionBlobField
from Products.Archetypes.atapi import FileWidget, AnnotationStorage
from Products.ATContentTypes.interface import IATFile
from Products.validation import V_REQUIRED
from Products.ATContentTypes import ATCTMessageFactory as _


class VirusFreeATFileExtender(object):
    """
    """
    adapts(IATFile)
    implements(ISchemaExtender)
    fields = [
        ExtensionBlobField('file',
                  required=True,
                  primary=True,
                  searchable=True,
                  languageIndependent=True,
                  storage = AnnotationStorage(migrate=True),
                  validators = (('isNonEmptyFile', V_REQUIRED),
                                ('checkFileMaxSize', V_REQUIRED),
                                ('isVirusFree', V_REQUIRED)),
                  widget = FileWidget(description='',
                                      label=_(u'label_file', default=u'File'),
                                      show_content_type=False)),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
