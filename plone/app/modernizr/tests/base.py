import unittest2 as unittest
from zope import interface
from plone.app import testing
from plone.app.modernizr.tests import layer


class UnitTestCase(unittest.TestCase):
    
    def setUp(self):
        super(UnitTestCase, self).setUp()

class TestCase(unittest.TestCase):

    layer = layer.INTEGRATION

    def setUp(self):
        from ZPublisher.tests.testPublish import Request
        super(TestCase, self).setUp()
        self.portal = self.layer['portal']
        self.request = Request()

class FunctionalTestCase(unittest.TestCase):

    layer = layer.FUNCTIONAL

    def setUp(self):
        super(FunctionalTestCase, self).setUp()
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])

def build_test_suite(test_classes):
    suite = unittest.TestSuite()
    for klass in test_classes:
        suite.addTest(unittest.makeSuite(klass))
    return suite
