from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="volunteers-list"),
    path("home/", views.volunteer_home, name="volunteer-home"),

    # TODO: implement volunteer profile with relevant permision checks
    # for editing or viewing permissions
    path(
      "profile/<int:volunteer_id>/",
      views.profile,
      name="volunteer-profile"),

    path(
      "profile/update/<int:volunteer_id>/",
      views.update_profile,
      name="volunteer-profile-update"),

    path(
      "skill_required/show_interest/<int:skill_required_id>/",
      views.show_interest_in_skill_required,
      name="show-interest-in-skill-required"),

    # TODO: implement
    path("skill/donate/create", views.create_skill_donate,
          name="create-skill-donation"),

    # TODO: implement
    path(
      "skills/donated/",
      views.skills_donated,
      name="volunteers-skills-donated"),

]
