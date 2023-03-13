from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Client, Shop, Product, Contact
from .forms import ClientForm, ShopForm, ProductForm

# Create your views here.




def Home(request):
    shop = Shop.objects.all
    context = {'shop':shop}
    return render(request, 'app/index.html', context)

# Hot
def Hot(request):
    pass

# Categories
def Fashion(request):
    pass

def Electronics(request):
    pass

def Jewellery(request):
    pass

def Delicasies(request):
    pass

def Automotive(request):
    pass

def Grocery(request):
    pass

def Cyber(request):
    pass

def Retail(request):
    pass

# Account
# <=====================================================>
def myAccount(request):
    client = request.user.client
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'app/account/my_account.html', context)

def Makeshop(request):
    owner = request.user
    form = ShopForm(initial={'owner':owner})
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'app/account/makeshop.html', context)
 
def addProduct(request, pk):
    product_owner = request.user
    product_shop = Shop.objects.get(id=pk)
    # shop = Shop.objects.get(id=pk)
    form = ProductForm(initial={'product_owner':product_owner,'product_shop':product_shop})
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'app/account/add_product.html', context)

def shopProduct(request, pk):
    shop_products = Product.objects.filter(id=pk)
    shop = Shop.objects.get(id=pk)
    all_products = shop.product_set.all()

    context = {'products': shop_products, 'shop':shop, 'all_products':all_products}
    return render(request, 'app/account/product.html', context)

def productDetails(request, pk):
    product = Product.objects.filter(id=pk)
    context = {'product':product}
    return render(request, 'app/account/product-details.html', context)

def myShop(request):
    product = Product.objects.all()
    shop = Shop.objects.all()
    context = {'shop':shop, 'product':product}
    return render(request, 'app/account/my_shops.html', context)


def updateShop(request, pk):
    shop = Shop.objects.get(id=pk)
    form = ShopForm(instance=shop)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            
            return redirect('my_shop')
    context = {'form':form, 'shop':shop}
    return render(request, 'app/account/makeshop.html', context)

def deleteShop(request, pk):
    shop = Shop.objects.get(id=pk)
    if request.method == 'POST':
        shop.delete()
        return redirect('my_shop')
    return render(request, 'app/delete.html', {'obj':shop})

def updateProduct(request, pk):
    product_owner = request.user
    product_shop = Shop.objects.get(id=pk)
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('my_shop')

    context = {'form':form}
    return render(request, 'app/account/add_product.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('my_shop')
    return render(request, 'app/delete.html', {'obj':product})

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if Client.objects.filter(username=username).exists():
                messages.error(request, 'Username exist')
                return redirect('register')
            elif Client.objects.filter(email=email).exists():
                messages.error(request, 'Email exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                client_details = Client.objects.create(user=user, username=user.username, email=email)
                client_details.save()

                messages.info(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password dont match')
            return redirect('register')
    else:
        return render(request, 'app/account/register.html')
    return render(request, 'app/account/register.html')

def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password,)

        if user is not None:
            auth.login(request, user)
            return redirect('my_account')
        else:
            messages.error(request, 'Invalid details')
            return redirect('login')
    else:
        return render(request, 'app/account/login.html')
    return render(request, 'app/account/login.html')

def logOut(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'app/account/logout.html')

# Other
def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        information = Contact.objects.create(name=name, email=email, message=message)
        information.save()
        
        messages.info(request, 'Message send successfully')
        return redirect('contact_us')
    
    return render(request, 'app/menu/contact.html')

def aboutUs(request):
    return render(request, 'app/menu/about.html')

def privacyPolicy(request):
    return render(request, 'app/menu/privacy-policy.html')




