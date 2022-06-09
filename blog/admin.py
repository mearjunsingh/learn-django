from django.contrib import admin

from .models import Blog, Category

admin.site.register(Category)


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "views", "created_at"]
    search_fields = ["title", "content"]
    # list_per_page = 1
    # date_hierarchy = "created_at"
    list_editable = ["views"]
    list_filter = ["category"]
    save_on_top = True

    fieldsets = (
        (
            "Post",
            {
                "fields": (("title", "views"), "content"),
            },
        ),
        (
            "test",
            {
                "fields": ["category", "image", "created_at"],
            },
        ),
    )

    readonly_fields = ["views", "created_at"]


admin.site.register(Blog, BlogAdmin)
