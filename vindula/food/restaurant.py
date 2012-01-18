# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.navigation.interfaces import INavigationRoot
from vindula.food import MessageFactory as _
from Products.CMFCore.utils import getToolByName
from vindula.controlpanel.vocabularies import ControlPanelObjects

from vindula.myvindula.user import BaseFunc
from vindula.food.models import ModelsRestaurantPreferences, ModelsSpecialty 
from vindula.food.content import IListRestaurantes

# Views
class VindulaFoodView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-food')

    
class RestaurantView(grok.View):
    grok.context(IListRestaurantes)
    grok.require('zope2.View')
    grok.name('restaurant')
    
    # Methods for Restaurant
    def get_restaurant(self):
        if 'id' in self.request.form.keys():
            id = int(self.request.get('id'))
            restaurant = ModelsRestaurantPreferences().get_food_restaurant().find(id = id).one()
            if restaurant:
                return restaurant
            else:
                return []
            
    def get_specialty(self, specialty_id):
             pass
         
class RestaurantsListView(grok.View):
    grok.context(IListRestaurantes)
    grok.require('zope2.View')
    grok.name('restaurantslist')
    
    # Methods for Restaurants List
    def get_restaurants(self, order='id'):
        if 'order' in self.request.form.keys():
            order = self.request.get('order')

        restaurants = ModelsRestaurantPreferences().get_food_restaurant(order)
        L = []
        if restaurants:
            for restaurant in restaurants:
                L.append(restaurant)
        return L
    
    def items_page(self):
        if 'size' in self.request.form.keys():
            return int(self.request.get('size'))
            
    
class RestaurantPreferencesView(grok.View, BaseFunc):
    grok.context(IListRestaurantes)
    grok.require('cmf.ManagePortal')
    grok.name('manage-restaurant')
    
    label = _(u"Configurar Restaurante")
    description = _(u"Change your available information below.")  
    
    # Methods for Restaurant
    def load_form(self):
        return ModelsRestaurantPreferences().registration_processes(self) 
    
    def get_specialties(self):
        data = ModelsSpecialty().get_food_specialty()
        if data.count() == 0:
            return []
        else:
            return data
    
class SpecialtyView(grok.View):
    grok.context(IListRestaurantes)
    grok.require('cmf.ManagePortal')
    grok.name('manage-specialty')

    # Methods for Specialty
    def load_form(self):
        return ModelsSpecialty().registration_processes(self)
    

