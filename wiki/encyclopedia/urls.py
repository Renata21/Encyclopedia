from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(f"<str:title>", views.get_page, name="entry"),
    path("wiki/search", views.search_page, name="search"),
    path("wiki/new", views.create_page, name="new"),
    path(f"wiki/edit/<str:title>", views.edit_page, name="edit"),
]
