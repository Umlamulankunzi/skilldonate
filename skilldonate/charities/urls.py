from django.urls import path

from . import views

urlpatterns = [
    path("", views.charities, name="charities-list"),
    path("home/", views.charity_home, name="charity-home"),
    path("skill_required/<int:skill_required_id>/", views.skill_required_detail, name="skill-required-detail"),
]
