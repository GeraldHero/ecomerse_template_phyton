from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

products = {
    "item1": {
        "id": 1,
        "image": "img-01.jpg",
        "format": "Digital Download",
        "views": 152,
        "date_posted": "2022-01-01",
        "name": "Modern Minimalist Living Room Decor",
        "description": "A set of minimalist living room decor prints featuring geometric shapes and neutral colors. Perfect for adding a touch of elegance to your living space.",
        "tags": ["Living Room", "Decor", "Prints", "Minimalist"]
    },
    "item2": {
        "id": 2,
        "image": "img-02.jpg",
        "format": "Physical Product",
        "views": 285,
        "date_posted": "2022-01-05",
        "name": "Wireless Bluetooth Earbuds",
        "description": "High-quality wireless earbuds with noise-cancellation feature and up to 15 hours of battery life. Comes with a charging case and multiple ear tips for a perfect fit.",
        "tags": ["Earbuds", "Wireless", "Headphones", "Noise-Cancellation"]
    },
    "item3": {
        "id": 3,
        "image": "img-03.jpg",
        "format": "Digital Download",
        "views": 97,
        "date_posted": "2022-01-10",
        "name": "Watercolor Floral Wedding Invitation Set",
        "description": "A set of beautiful watercolor floral wedding invitations featuring delicate flowers and elegant typography. Includes invitation, RSVP card, and details card.",
        "tags": ["Wedding", "Invitations", "Watercolor", "Floral"]
    },
    "item4": {
        "id": 4,
        "image": "img-04.jpg",
        "format": "Physical Product",
        "views": 521,
        "date_posted": "2022-01-15",
        "name": "Smart Home Security Camera",
        "description": "A high-quality security camera that connects to your home WiFi network and provides 24/7 surveillance. Features motion detection, night vision, and remote access via smartphone app.",
        "tags": ["Smart Home", "Security", "Camera", "WiFi"]
    },
    "item5": {
        "id": 5,
        "image": "img-05.jpg",
        "format": "Physical Product",
        "views": 182,
        "date_posted": "2022-01-20",
        "name": "Men's Leather Messenger Bag",
        "description": "A stylish and durable messenger bag made from high-quality leather. Features multiple compartments and pockets for storage and organization.",
        "tags": ["Men", "Leather", "Messenger Bag", "Fashion"]
    },
    "item6": {
        "id": 6,
        "image": "img-06.jpg",
        "format": "Physical Product",
        "views": 305,
        "date_posted": "2022-01-25",
        "name": "Wireless Charging Pad",
        "description": "A sleek and modern wireless charging pad that works with all Qi-enabled devices. Charges your phone quickly and efficiently without the hassle of cords.",
        "tags": ["Wireless", "Charging Pad", "Technology", "Qi-enabled"]
    },
    "item8": {
        "id": 7,
        "image": "img-08.jpg",
        "format": "Digital Download",
        "views": 67,
        "date_posted": "2022-02-05",
        "name": "Instagram Story Templates",
        "description": "A set of 10 customizable Instagram story templates featuring trendy designs and bold colors. Perfect for bloggers, influencers, and small business owners.",
        "tags": ["Instagram", "Story Templates", "Social Media", "Design"]
    },
    "item9": {
        "id": 9,
        "image": "img-09.jpg",
        "format": "Physical Product",
        "views": 449,
        "date_posted": "2022-02-10",
        "name": "Wireless Gaming Headset",
        "description": "A high-quality wireless gaming headset with immersive 7.1 surround sound and noise-cancellation feature. Features a long battery life and comfortable over-ear design.",
        "tags": ["Gaming", "Headset", "Wireless", "Surround Sound"]
    },
    "item10": {
        "id": 10,
        "image": "img-10.jpg",
        "format": "Physical Product",
        "views": 273,
        "date_posted": "2022-02-15",
        "name": "Smartwatch",
        "description": "A sleek and stylish smartwatch with a variety of features, including heart rate monitor, GPS tracking, and smartphone notifications. Perfect for fitness enthusiasts and tech lovers.",
        "tags": ["Smartwatch", "Technology", "Fitness", "Notifications"]
    },
    "item11": {
        "id": 11,
        "image": "img-11.jpg",
        "format": "Physical Product",
        "views": 187,
        "date_posted": "2022-02-20",
        "name": "Leather Travel Wallet",
        "description": "A practical and stylish leather travel wallet with multiple compartments and card slots. Perfect for organizing your passport, tickets, and other travel essentials.",
        "tags": ["Travel", "Wallet", "Leather", "Organizer"]
    },
    "item12": {
        "id": 12,
        "image": "img-12.jpg",
        "format": "Digital Download",
        "views": 52,
        "date_posted": "2022-02-25",
        "name": "Printable Meal Planner",
        "description": "A printable meal planner with space for breakfast, lunch, dinner, and snacks. Features a grocery list section and a water intake tracker. Perfect for keeping your diet on track.",
        "tags": ["Meal Planner", "Printable", "Diet", "Healthy Eating"]
    }
}
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


def videoPage(request):
    return render(request, 'base/video.html')


def aboutPage(request):
    return render(request, 'base/about.html')


def contactPage(request):
    return render(request, 'base/contact.html')
