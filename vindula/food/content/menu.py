# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import schemata, base


from vindula.food.content.interfaces import IMenu
from vindula.food import MessageFactory as _
from vindula.food.config import *


from vindula.content.content.vindulanews import VindulaNews, VindulaNews_schema


Menu_schema = VindulaNews_schema.copy() + Schema((


    StringField(
        name='dias',
        widget=SelectionWidget(label=_(u"Dia do Prato"),
                               description=_(u"Selecione em qual dia o prato e servido."),
                               ),
        required=True,
        vocabulary='voc_dias',
    ),


))

invisivel = {'view':'invisible','edit':'invisible',}
Menu_schema['activ_image'].widget.visible = invisivel
Menu_schema['active_date'].widget.visible = invisivel
Menu_schema['active_author'].widget.visible = invisivel
Menu_schema['activ_share'].widget.visible = invisivel
Menu_schema['activ_share_footer'].widget.visible = invisivel


schemata.finalizeATCTSchema(Menu_schema, folderish=False)

class Menu(base.ATCTContent):
    """ Reserve Content for Menu """
    security = ClassSecurityInfo()

    implements(IMenu)
    portal_type = 'Menu'
    _at_rename_after_creation = True
    schema = Menu_schema

    def voc_dias(self):
        dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        retorno = []
        for dia in dias:
            retorno.append((dia, dia))

        return DisplayList(tuple(retorno))


registerType(Menu, PROJECTNAME)

