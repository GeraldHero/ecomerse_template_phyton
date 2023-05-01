from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homePage, name='home'),
    path('photo/', views.photoPage, name='photo'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name='register'),
    path('photo/<int:pk>', views.photoPageProduct, name='photo-product'),
    path('video/', views.videoPage, name='video'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('product/add/', views.addItem, name='add_product'),
    path('cart/<str:pk>', views.cartPage, name='cart'),
    path('buy', views.buyPage, name='buy'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
