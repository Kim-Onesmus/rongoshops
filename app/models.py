from django.db import models
from django.contrib.auth.models import auth, User

# Create your models here.



class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True)
    username = models.CharField(max_length=25, null=True)
    number = models.PositiveIntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return(self.username)
    
    
class Shop(models.Model):
    CATEGORY_CHOICES = [
    ("fashion","fashion"),
    ("jewellery","jewellery"),
    ("electronics","electronics"),
    ("automotive","automotive"),
    ("cyber","cyber"),
    ("elicasies","delicasies"),
    ("grocery","grocery"),
    ("retail","retail"),
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/')  
      
    def __str__(self):
        return(self.name)
    
    
class Product(models.Model):
    DELIVERY_CHOICES = [
    ("free delivery", "free delivery"),
    ("no delivery", "no delivery"),
    ]
    product_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    delivery = models.CharField(max_length=15, choices=DELIVERY_CHOICES)
    instock = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return(self.product_name)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    
    def __str__(self):
        return(self.name)