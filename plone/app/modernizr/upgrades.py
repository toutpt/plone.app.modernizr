from Products.CMFCore.utils import getToolByName

def remove_plone3rdParty_modernizr(context):
    """This is the future upgrade that will be applied to Plone"""
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.unregisterResource('modernizr.js')
    jsregistry.cookResources()
