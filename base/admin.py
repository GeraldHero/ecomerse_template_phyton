from django.contrib import admin
from .models import Image, Product, Tag, Format
# Register your models here.
admin.site.register([Image, Product, Tag, Format])
