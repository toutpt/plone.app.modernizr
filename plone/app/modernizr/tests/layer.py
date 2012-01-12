from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class JSLayer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.modernizr
        self.loadZCML(package=plone.app.modernizr)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'plone.app.modernizr:default')


FIXTURE = JSLayer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                                 name="plone.app.modernizr:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                               name="plone.app.modernizr:Functional")
