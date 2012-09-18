# -*- coding: utf-8 -*-

#Imports regarding the connection of the database 'storm'
from storm.locals import *
from Products.statusmessages.interfaces import IStatusMessage
from vindula.myvindula.validation import valida_form
from vindula.myvindula.validation import to_utf8

from Products.CMFCore.utils import getToolByName

from vindula.myvindula.models.base import BaseStore



class ModelsRestaurantPreferences(Storm, BaseStore):
    __storm_table__ = 'vin_food_restaurant'
    _name_class = 'ModelsRestaurantPreferences'
    
    id = Int(primary=True)
    name = Unicode()
    vin_food_specialty_id = Int()
    address = Unicode()
    phone_number = Unicode()
    delivery = Bool()
    opening_hours = Unicode()
    has_agreement = Bool()
    agreement = Unicode()

    specialty = Reference(vin_food_specialty_id, "ModelsSpecialty.id")
    
        
        
    #-------------- Loads and Methods data into DataBase --------------------#
                               
    def get_food_restaurant(self, order='id'):
        if order == 'name':
            data = self.store.find(ModelsRestaurantPreferences).order_by(ModelsRestaurantPreferences.name)
        else:
            data = self.store.find(ModelsRestaurantPreferences).order_by(Desc(ModelsRestaurantPreferences.id))  
            
        if data:
            return data
        else:
            return None
    
    def set_food_restaurant(self,**kwargs):
        D={}
        D['name']                  = unicode(kwargs.get('name'              ,''))
        D['vin_food_specialty_id'] = kwargs.get('vin_food_specialty_id'     ,'')
        D['address']               = unicode(kwargs.get('address'           ,''))
        D['phone_number']          = unicode(kwargs.get('phone_number'      ,''))
        D['delivery']              = kwargs.get('delivery'                  ,False)
        D['opening_hours']         = unicode(kwargs.get('opening_hours'     ,''))
        D['has_agreement']         = kwargs.get('has_agreement'             ,False)
        D['agreement']             = unicode(kwargs.get('agreement'         ,''))
        
        # adicionando...
        restaurant = ModelsRestaurantPreferences(**D)
        self.store.add(restaurant)
        self.store.flush()
                               
    def registration_processes(self, ctx):
        success_url = ctx.context.absolute_url() + '/edit-restaurant'
        access_denied = ctx.context.absolute_url() + '/login'
        form = ctx.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        campos = {
                  'name'                 : {'required': True , 'type': to_utf8}, #campo obrigatorio
                  'vin_food_specialty_id': {'required': True , 'type': int    }, #campo obrigatorio
                  'address'              : {'required': True , 'type': to_utf8}, #campo obrigatorio
                  'phone_number'         : {'required': False, 'type': to_utf8},
                  'delivery'             : {'required': False, 'type': bool   },
                  'opening_hours'        : {'required': False, 'type': to_utf8},
                  'has_agreement'        : {'required': False, 'type': bool   }, 
                  'agreement'            : {'required': False, 'type': to_utf8}
                 } 
        
        # divisao dos dicionarios "errors" e "convertidos"
        form_data = {
            'errors': {},
            'data': {},
            'campos':campos,}
        # se clicou no botao "Voltar"
        if 'form.voltar' in form_keys:
            ctx.request.response.redirect(success_url)
          
        # se clicou no botao "Salvar"
        elif 'form.submited' in form_keys:
            # Inicia o processamento do formulario
            # chama a funcao que valida os dados extraidos do formulario (valida_form) 
            errors, data = valida_form(campos, form)  

            if not errors:
                
                if 'id' in form_keys:
                    # editando...
                    id = int(form.get('id'))
                    result = self.get_food_restaurant().find(id = id).one()
                    success_url = ctx.context.absolute_url() + '/restaurant?id='+str(id)
                    if result:
                        for campo in campos.keys():
                            value = data.get(campo, None)
                            setattr(result, campo, value)

                else:
                    #adicionando...
                    self.set_food_restaurant(**data)
                        
                #Redirect back to the front page with a status message
                #IStatusMessage(ctx.request).addStatusMessage(_(u"Thank you for your order. We will contact you shortly"), "info")
                ctx.request.response.redirect(success_url)
                                   
            else:
                form_data['errors'] = errors
                form_data['data'] = data
                return form_data
        
        # se clicou em excluir
        elif 'form.delete' in form_keys:
            p_utils = getToolByName(ctx.context, 'plone_utils')
            if 'id' in form_keys:
                record = self.get_food_restaurant().find(id = int(form.get('id'))).one()
                self.store.remove(record)
                self.store.flush()
                p_utils.addPortalMessage('Removido com sucesso.', 'info')
                ctx.request.response.redirect(ctx.context.absolute_url())
        
        # se for um formulario de edicao 
        elif 'id' in form_keys:
            id = int(form.get('id'))
            data = self.get_food_restaurant().find(id = id).one()
            
            D = {}
            for campo in campos.keys():
                D[campo] = getattr(data, campo, '')
              
            if data:
               form_data['data'] = D
               return form_data
            else:
               return form_data
              
        # se o usuario não estiver logado
        else:
            return form_data
        
class ModelsSpecialty(Storm, BaseStore):
    __storm_table__ = 'vin_food_specialty'
    _name_class = 'ModelsSpecialty'
    
    id = Int(primary=True)
    name = Unicode()
    
    #------------------------ Loads and Methods data into DataBase ---------------------#
    def get_food_specialty(self):
        data = self.store.find(ModelsSpecialty)
        if data:
            return data
        else:
            return None
        
    def set_food_specialty(self, **kwargs):
        #pegando os dados a serem adicionados
        D={}
        D['name'] = unicode(kwargs.get('name',''))
        
        #adicionando...
        specialty = ModelsSpecialty(**D)
        self.store.add(specialty)
        self.store.flush()
    
    def registration_processes(self, ctx):
        success_url = ctx.context.absolute_url() + '/edit-specialty'
        access_denied = ctx.context.absolute_url() + '/login'
        form = ctx.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        campos = {
                  'name': {'required': True , 'type': to_utf8} #campo obrigatorio
                 } 
        
        if 'rest_id' in form_keys:
            if form.get('rest_id') != 'None':
                success_url = ctx.context.absolute_url() + '/manage-restaurant?id=' + form.get('rest_id')
        
        # divisao dos dicionarios "errors" e "convertidos"
        form_data = {
            'errors': {},
            'data': {},
            'campos':campos,}
        
        # se clicou no botao "Voltar"
        if 'form.voltar' in form_keys:
            ctx.request.response.redirect(success_url)
          
        # se clicou no botao "Salvar"
        elif 'form.submited' in form_keys:
            # Inicia o processamento do formulario
            # chama a funcao que valida os dados extraidos do formulario (valida_form) 
            errors, data = valida_form(campos, form)  
            
            if not errors:
                if 'id' in form_keys:
                    # editando...
                    id = int(form.get('id'))
                    result = self.get_food_specialty().find(id = id).one()
                    if result:
                        for campo in campos.keys():
                            value = data.get(campo, None)
                            setattr(result, campo, value)

                else:
                    #adicionando...
                    self.set_food_specialty(**data)
                        
                #Redirect back to the front page with a status message
                #IStatusMessage(ctx.request).addStatusMessage(_(u"Thank you for your order. We will contact you shortly"), "info")
                ctx.request.response.redirect(success_url)
                                   
            else:
                form_data['errors'] = errors
                form_data['data'] = data
                return form_data
          
        # se clicou no botão "Excluir"
        elif 'form.delete' in form_keys:
            if 'id' in form_keys:
                result = ModelsRestaurantPreferences().get_food_restaurant().find(vin_food_specialty_id = int(form.get('id')))
                if result.count() == 0:
                    record = self.get_food_specialty().find(id = int(form.get('id'))).one()
                    self.store.remove(record)
                    self.store.flush()
                    
                    ctx.request.response.redirect(success_url)
                else:
                    ctx.request.response.redirect(ctx.context.absolute_url() + '/manage-specialty"?error=true&id=' + form.get('id'))

        # se for um formulario de edicao 
        elif 'id' in form_keys:
            id = int(form.get('id'))
            data = self.get_food_specialty().find(id = id).one()
            
            D = {}
            for campo in campos.keys():
                D[campo] = getattr(data, campo, '')
              
            if data:
               form_data['data'] = D
               return form_data
            else:
               return form_data
              
        # se o usuario não estiver logado
        else:
            return form_data