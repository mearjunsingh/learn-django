from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .forms import AddPostForm
from .models import Blog, Category


def index_page(request):
    blogs = Blog.objects.all().order_by("-created_at")

    paginator = Paginator(blogs, 3)

    page = request.GET.get("page")

    blogs = paginator.get_page(page)

    ctx = {"blogs": blogs}

    return render(request, "index.html", ctx)


def single_page(request, id):
    blog = Blog.objects.get(id=id)
    blog.views += 1
    blog.save()
    print(blog.views)
    ctx = {"blog": blog}
    return render(request, "single.html", ctx)


def archive_page(request):
    cat_query = request.GET.get("cat")
    search_query = request.GET.get("search")

    if cat_query:
        cat_obj = Category.objects.get(slug=cat_query)
        blogs = Blog.objects.filter(category=cat_obj)

    elif search_query:
        blogs = Blog.objects.filter(title__icontains=search_query)

    else:
        blogs = None

    ctx = {"blogs": blogs}

    return render(request, "archive.html", ctx)


@login_required(login_url="/admin")
def dashboard_page(request):
    blogs = Blog.objects.all().order_by("-created_at")

    paginator = Paginator(blogs, 3)

    page = request.GET.get("page")

    blogs = paginator.get_page(page)

    ctx = {"blogs": blogs}
    return render(request, "dashboard.html", ctx)


@login_required(login_url="/admin")
def add_post_page(request):

    form = AddPostForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard_page")

    ctx = {"form": form}
    return render(request, "post-form.html", ctx)


@login_required(login_url="/admin")
def edit_post_page(request, id):

    blog = Blog.objects.get(id=id)

    form = AddPostForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("dashboard_page")

    ctx = {"form": form}

    return render(request, "post-form.html", ctx)
