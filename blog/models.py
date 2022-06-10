from ckeditor.fields import RichTextField
from django.db import models

from .utils import upload_image_path


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "kategory"
        verbose_name_plural = "kategories"


class Blog(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=50)
    content = RichTextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    views = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
