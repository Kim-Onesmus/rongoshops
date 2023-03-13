from django.forms import ModelForm, TextInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client, Shop, Product
from django import forms

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['user']
        
        
class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        