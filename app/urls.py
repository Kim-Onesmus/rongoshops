from django.urls import path
from . import  views

urlpatterns = [
    path('', views.Home, name='home'),
    
    # Hot
    path('hot', views.Hot, name='hot'),
    
	# path('cart/', views.cart, name="cart"),
    
    # Categories
    path('fashion', views.Fashion, name='fashion'),
    path('electronics', views.Electronics, name='electronics'),
    path('jewellery', views.Jewellery, name='jewellery'),
    path('delicasies', views.Delicasies, name='delicasies'),
    path('automotive', views.Automotive, name='automotive'),
    path('grocery', views.Grocery, name='grocery'),
    path('cyber', views.Cyber, name='cyber'),
    path('retail', views.Retail, name='retail'),
    
    
    
    # Account
    path('my_account', views.myAccount, name='my_account'),
    path('shopproduct/<str:pk>/', views.shopProduct, name='shopproduct'),
    path('productdetails/<str:pk>/', views.productDetails, name='productdetails'),
    path('makeshop', views.Makeshop, name='makeshop'),
    path('add_product/<str:pk>/', views.addProduct, name='add_product'),
    path('my_shop', views.myShop, name='my_shop'),
    path('register', views.Register, name='register'),
    path('login', views.logIn, name='login'),
    path('logout', views.logOut, name='logout'),
    
    # Changes
    path('update-shop/<str:pk>/', views.updateShop, name="update-shop"),
    path('delete-shop/<str:pk>/', views.deleteShop, name="delete-shop"),
    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),
    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),
    
    # Other
    path('contact_us', views.contactUs, name='contact_us'),
    path('about_us', views.aboutUs, name='about_us'),
    path('privacy_policy', views.privacyPolicy, name='privacy_policy'),



]