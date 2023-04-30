from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
         
        try:
            user = User.objects.get(email=username)
             
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, email=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print(user)
            messages.error(request, 'Username OR password does not exit')
             
    return render(request, 'base/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    return render(request, 'base/login_register.html')


def homePage(request):
    # https://docs.djangoproject.com/en/4.2/topics/pagination/
    products = Product.objects.get_queryset().order_by('id')
    paginator = Paginator(products, 10)  # Show 10 contacts per page.

    # get the url page value
    page_number = request.GET.get("page")

    # update paginator value
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj":  page_obj
    }
    return render(request, 'base/index.html', context)


def addItem(request):
    if (request.method == 'POST'):
        product_name = request.POST.get('item_name')

    context = {}
    return render(request, 'base/add_product.html', context)


def photoPage(request):
    products = Product.objects.all()
    context = {
        "page_obj": products
    }
    return render(request, 'base/photo.html', context)


def photoPageProduct(request, pk):
    product = Product.objects.get(id=pk)
    tags = product.tags.all()
    # for key, product in products.items():
    # for key, value in products.items():
    #     if (value['id'] == pk):
    #         context = {
    #             "product": value
    #         }
    #         return render(request, 'base/product_view.html', context)
    # print(f"ID of {key}: {value['id']}")
    context = {
        "product": product,
        "tags": tags
    }
    return render(request, 'base/product_view.html', context)

def cartPage(request, pk):
    context = {}
    return render(request, 'base/cart.html', context)

def buyPage(request, pk):
    context = {}
    return render(request, 'base/buy.html', context)

def videoPage(request):
    return render(request, 'base/video.html')


def aboutPage(request):
    return render(request, 'base/about.html')


def contactPage(request):
    return render(request, 'base/contact.html')
