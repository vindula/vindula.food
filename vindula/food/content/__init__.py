# -*- coding: utf-8 -*-

from zope import schema

from plone.directives import form, dexterity
from vindula.food import MessageFactory as _

import restaurants
import menu



# Interface and schema
class IListRestaurantes(form.Schema):
    """ Restaurantes """



