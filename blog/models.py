from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
