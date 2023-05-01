from django.contrib import admin
from .models import User, Image, Product, Tag, Format
# Register your models here.
admin.site.register([User, Image, Product, Tag, Format])
