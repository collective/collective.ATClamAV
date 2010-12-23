from plone.app.blob.subtypes.image import SchemaExtender as oldSchemaExtender
from .atimage import VirusFreeATImageExtender
oldSchemaExtender = VirusFreeATImageExtender