from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.random_page, name="random_page"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("add/", views.add, name="add"),
    path("search/", views.search, name="search"),
    path("edit/<str:title>", views.edit, name="edit")
]
