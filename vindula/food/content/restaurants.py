# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from plone.app.folder.folder import ATFolder
from Products.ATContentTypes.content.schemata import finalizeATCTSchema


from vindula.food.content.interfaces import IRestaurants
from vindula.food import MessageFactory as _
from vindula.food.config import *

Restaurants_schema = ATFolder.schema.copy() + Schema((



))

finalizeATCTSchema(Restaurants_schema, folderish=True)

class Restaurants(ATFolder):
    """ Reserve Content for Restaurants """
    security = ClassSecurityInfo()

    implements(IRestaurants)
    portal_type = 'Restaurants'
    _at_rename_after_creation = True
    schema = Restaurants_schema



registerType(Restaurants, PROJECTNAME)

