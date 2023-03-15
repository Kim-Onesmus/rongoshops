from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Client, Shop, Product, Contact, Order, OrderItem
from .forms import ClientForm, ShopForm, ProductForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
import json


# Create your views here.




def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    product = Product.objects.filter(
        # Q(product_owner__icontains=q) |
        # Q(product_shop__icontains=q) |
        Q(product_name__icontains=q) |
        Q(delivery__icontains=q) |
        Q(new_price__icontains=q) |
        Q(old_price__icontains=q) |
        Q(description__icontains=q)
    )
    
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    
    product_count = product.count()
    shop = Shop.objects.all
    context = {'shop':shop, 'product_count':product_count, 'product':product, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/index.html', context)

# Hot
def Hot(request):
    pass


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    
    client = request.user.client
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(client=client, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse('Item was added', safe=False)


def cart(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'app/cart.html', context)


# Categories
def Fashion(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/fashion.html', context)

def Electronics(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/electronics.html', context)


def Jewellery(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/jewellery.html', context)


def Delicasies(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/delicasies.html', context)

def Automotive(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/automotive.html', context)

def Grocery(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/grocery.html', context)

def Cyber(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/cyber.html', context)

def Retail(request):
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    shop = Shop.objects.all
    context = {'shop':shop, 'cartItems':cartItems, 'items':items,}
    return render(request, 'app/categories/retail.html', context)

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
        
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'form':form}
    return render(request, 'app/account/my_account.html', context)

def Makeshop(request):
    owner = request.user
    form = ShopForm(initial={'owner':owner})
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_shop')
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
            return redirect('my_shop')

    context = {'form':form}
    return render(request, 'app/account/add_product.html', context)

def shopProduct(request, pk):
    shop_products = Product.objects.filter(id=pk)
    shop = Shop.objects.get(id=pk)
    all_products = shop.product_set.all()

    context = {'products': shop_products, 'shop':shop, 'all_products':all_products}
    return render(request, 'app/account/product.html', context)

def productDetails(request, pk):
    products = Product.objects.filter(id=pk)
    
    if request.user.is_authenticated:
        client = request.user.client
        order, created = Order.objects.get_or_create(client=client, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems}
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




