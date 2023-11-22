from django.urls import path

from .views import search_site

urlpatterns = [
    path("", search_site, name="search"),
]
