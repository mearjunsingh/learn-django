from django.urls import path

from .views import (
    add_post_page,
    archive_page,
    dashboard_page,
    index_page,
    single_page,
    edit_post_page,
)

urlpatterns = [
    path("", index_page, name="index"),
    path("add/", add_post_page, name="add_post"),
    path("edit/<int:id>/", edit_post_page, name="edit_post"),
    path("archive/", archive_page, name="archive_page"),
    path("dashboard/", dashboard_page, name="dashboard_page"),
    path("<int:id>/", single_page, name="single"),
]
