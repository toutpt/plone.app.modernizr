from plone.app.modernizr.tests import base

OLD_JS = 'modernizr.js'
JS = '++resource++plone.app.modernizr/modernizr.js'
PROFILE = 'plone.app.modernizr:default'

class TestIntegration(base.TestCase):

    def test_jsregistry(self):
        jsregistry = self.portal.portal_javascripts
        modernizr = jsregistry.getResource(OLD_JS)
        self.failUnless(not modernizr.getEnabled())
        new_modernizr = jsregistry.getResource(JS)
        self.failUnless(new_modernizr.getEnabled())

    def test_upgrade(self):
        from Products.GenericSetup.upgrade import listUpgradeSteps
        setup = self.portal.portal_setup
        steps = listUpgradeSteps(setup, PROFILE, None)
        step_id = steps[0]['id']
        request = self.portal.REQUEST
        request.form['upgrades'] = [step_id]
        request.form['profile_id'] = PROFILE
        setup.manage_doUpgrades()
        
        jsregistry = self.portal.portal_javascripts
        modernizr = jsregistry.getResource(OLD_JS)
        self.failUnless(modernizr is None)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return base.build_test_suite((TestIntegration,))
