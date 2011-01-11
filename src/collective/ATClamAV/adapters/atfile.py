from archetypes.schemaextender.interfaces import ISchemaModifier
from Products.ATContentTypes.interface import IATFile
from zope.component import adapts
from zope.interface import implements


class VirusFreeATFileModifier(object):
    """
    """
    adapts(IATFile)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        schema['file'].validators.appendRequired('isVirusFree')
