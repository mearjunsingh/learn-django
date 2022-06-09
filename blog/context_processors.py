from .forms import SearchForm
from .models import Blog, Category


def menu_categories(request):
    cats = Category.objects.all()

    search_form = SearchForm(request.GET or None)

    all_posts = Blog.objects.all()
    ordered_posts = all_posts.order_by("-views")
    popular_posts = ordered_posts[:5]

    ctx = {
        "category_menu": cats,
        "popular_posts": popular_posts,
        "search_form": search_form,
    }

    return ctx
