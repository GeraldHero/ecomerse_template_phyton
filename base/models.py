from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
import os
from django.utils import timezone


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


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


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).file
    except Image.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class Product(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    views = models.CharField(max_length=200, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    item_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    sale_price = models.CharField(max_length=200, blank=True)
    original_price = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(
        Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.item_name
