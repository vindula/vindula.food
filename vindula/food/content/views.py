# -*- coding: utf-8 -*-
from five import grok

from vindula.food.content import IListRestaurantes

grok.templatedir('templates')

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
