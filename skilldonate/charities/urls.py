from django.urls import path

from . import views

urlpatterns = [
    path("", views.charities, name="charities-list"),
    path("home/", views.charity_home, name="charity-home"),
    path("profile/<int:user_id>/", views.profile, name="charity-profile"),
    path("profile/update/<int:user_id>/", views.update_profile,
          name="charity-profile-update"),
    path("skill_required/<int:skill_required_id>/", views.skill_required_detail, name="skill-required-detail"),
    path("skill_required/create/", views.create_skill_request, name="create-skill-required"),
]
