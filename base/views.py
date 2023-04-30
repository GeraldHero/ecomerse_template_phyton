from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
 
# Create your views here.


def loginPage(request):
    return render(request, 'base/login_register.html')


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
