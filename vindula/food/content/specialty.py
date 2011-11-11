# -*- coding: utf-8 -*-
from zope import schema
from plone.directives import form
from vindula.food import MessageFactory as _

# Interface and schema

class ISpecialty(form.Schema):
    """ Specialty """
    
    spestructure = schema.Text(
        title=_(u"Especialidades dos restaurantes"),
        description=_(u"Adicione uma especialidade por linha."),
        required=False,
        )    
