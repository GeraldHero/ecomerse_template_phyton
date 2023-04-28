from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
import os
from django.utils import timezone


def rename_image(instance, filename):
    # Get the file extension from the original filename
    ext = os.path.splitext(filename)[1]

    # Generate a new filename based on the current date and time
    new_filename = timezone.now().strftime('%Y%m%d%H%M%S') + ext

    return new_filename
# Create your models here.

# https://stackoverflow.com/questions/25386119/whats-the-difference-between-a-onetoone-manytomany-and-a-foreignkey-field-in-d


class Format(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(models.signals.pre_save, sender=Image)
def update_image_filename(sender, instance, **kwargs):
    if instance.image:
        instance.image.name = rename_image(instance, instance.image.name)


class ProductVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.user


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    # views = models.ForeignKey(ProductVisit, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(
        Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.item_name
