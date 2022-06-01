from django.shortcuts import render

from .models import Blog


def index_page(request):
    blogs = Blog.objects.all().order_by("-created_at")
    ctx = {"blogs": blogs}
    return render(request, "index.html", ctx)


def single_page(request, id):
    blog = Blog.objects.get(id=id)
    ctx = {"blog": blog}
    return render(request, "single.html", ctx)
