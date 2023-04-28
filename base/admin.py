from django.contrib import admin
from .models import Image, Product, ProductVisit, Tag, Format
# Register your models here.
admin.site.register([Image, Product, ProductVisit, Tag, Format])
