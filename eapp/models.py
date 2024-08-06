import uuid
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class ImageModel(models.Model):
    reference_id = models.CharField(max_length=32,unique=True,  primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    content = FroalaField()
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class AuthModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
