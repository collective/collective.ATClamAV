from archetypes.schemaextender.interfaces import ISchemaModifier
from Products.ATContentTypes.interfaces.image import IATImage
from zope.component import adapts
from zope.interface import implements


class VirusFreeATImageModifier(object):
    """
    """
    adapts(IATImage)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        schema['image'].validators.appendRequired('isVirusFree')
