# -*- coding: utf-8 -*-
from five import grok
from zope import schema

from plone.directives import form, dexterity
from vindula.food import MessageFactory as _


# Interface and schema
class IListRestaurantes(form.Schema):
    """ Restaurantes """



#view
class ListRestauranstesView(grok.View):
    grok.context(IListRestaurantes)
    grok.require('zope2.View')
    grok.name('view')
    
    
    

class EditEspecialidadeView(grok.View):
    grok.context(IListRestaurantes)
    grok.require('cmf.ManagePortal')
    grok.name('edit-specialty')
    
    
    

class EditRestauranstesView(grok.View):
    grok.context(IListRestaurantes)
    grok.require('cmf.ManagePortal')
    grok.name('edit-restaurant')
        