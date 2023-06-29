from django.urls import path
from django.contrib.auth import views as auth_views
from . import  views

urlpatterns = [
    path('', views.Home, name='home'),
    
    path('search', views.Search, name='search'),
    
    
    # Hot
    path('hot', views.Hot, name='hot'),
    
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),

    
    
    # Categories
    path('fashion', views.Fashion, name='fashion'),
    path('electronics', views.Electronics, name='electronics'),
    path('jewellery', views.Jewellery, name='jewellery'),
    path('delicasies', views.Delicasies, name='delicasies'),
    path('automotive', views.Automotive, name='automotive'),
    path('grocery', views.Grocery, name='grocery'),
    path('cyber', views.Cyber, name='cyber'),
    path('retail', views.Retail, name='retail'),
    
    #M-Pesa
    path('lipa', views.Lipa, name='lipa'), 
    
    # Account
    path('my_account', views.myAccount, name='my_account'),
    path('shopproduct/<str:pk>/', views.shopProduct, name='shopproduct'),
    path('productdetails/<str:pk>/', views.productDetails, name='productdetails'),
    path('makeshop', views.Makeshop, name='makeshop'),
    path('add_product/<str:pk>/', views.addProduct, name='add_product'),
    path('my_shop', views.myShop, name='my_shop'),
    path('register', views.Register, name='register'),
    path('logout', views.logOut, name='logout'),
    
    # Password reset
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="app/passwordReset/forget-password.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="app/passwordReset/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="app/passwordReset/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="app/passwordReset/password_reset_done.html"), 
        name="password_reset_complete"),
    
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