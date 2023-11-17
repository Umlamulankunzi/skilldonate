from django.urls import path

from . import views

urlpatterns = [
    path("", views.charities, name="charities-list"),
]
