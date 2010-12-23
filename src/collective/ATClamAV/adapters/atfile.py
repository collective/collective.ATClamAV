from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.atapi import FileWidget, AnnotationStorage
from plone.app.blob.field import BlobField
from Products.ATContentTypes.interface import IATFile
from Products.validation import V_REQUIRED
from Products.ATContentTypes import ATCTMessageFactory as _


class VirusFreeFileField(ExtensionField, BlobField):
    """
    """


class VirusFreeATFileExtender(object):
    """
    """
    adapts(IATFile)
    implements(ISchemaExtender)
    fields = [
        VirusFreeFileField('file',
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
