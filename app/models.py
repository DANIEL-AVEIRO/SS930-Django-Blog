from django.db import models
import uuid

# Create your models here.


class CategoryModel(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostModel(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="posts", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
