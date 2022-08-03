from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(f"<str:title>", views.get_page, name = "entry"),
    path("/search", views.search_page, name = "search")
]
