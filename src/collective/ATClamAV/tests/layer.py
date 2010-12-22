from transaction import commit
from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing.ZopeTestCase import app, close, installPackage
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.layer import PloneSite


class ATClamAVLayer(PloneSite):

    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        import collective.ATClamAV
        zcml.load_config('configure.zcml', collective.ATClamAV)
        fiveconfigure.debug_mode = False
        installPackage('collective.ATClamAV', quiet=True)
        # import the default profile
        root = app()
        portal = root.plone
        tool = getToolByName(portal, 'portal_setup')
        profile = 'profile-collective.ATClamAV:default'
        tool.runAllImportStepsFromProfile(profile, purge_old=False)
        # and commit the changes
        commit()
        close(root)
