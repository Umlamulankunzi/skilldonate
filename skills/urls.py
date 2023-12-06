from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="skills-list"),
    # path("required/", views.required_skills, name="skills-required"),
]
