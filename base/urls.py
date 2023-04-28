from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('photo/', views.photoPage, name='photo'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('photo/<int:pk>', views.photoPageProduct, name='photo-product'),
    path('video/', views.videoPage, name='video'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('product/add/', views.addItem, name='add_product')
]
