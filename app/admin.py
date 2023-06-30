from django.contrib import admin
from .models import Client, Shop, Product, Contact, LipaNaMpesa

# Register your models here.

@admin.register(Client)
class ClientTable(admin.ModelAdmin):
    list_display = ('user','name','username','number','email','profile_pic')
    
    
@admin.register(Shop)
class ShopTable(admin.ModelAdmin):
    list_display = ('owner', 'name', 'category', 'location', 'image')
    
    
@admin.register(Product)
class ProductTable(admin.ModelAdmin):
    list_display = ('product_owner', 'product_shop', 'product_name', 'image', 'delivery', 'instock', 'new_price', 'old_price', 'description')
    
    
@admin.register(Contact)
class ContactTable(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    
@admin.register(LipaNaMpesa)
class LipaNaMpesa(admin.ModelAdmin):
    list_display = ('short_code', 'reference')