from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = "homepage.html"), name="logout"),
    path("signup/volunteer", views.VolunteerSignUpView.as_view(), name="signup-volunteer"),
    path("signup/charity", views.CharitySignUpView.as_view(), name="signup-charity"),

]

# LOGIN_REDIRECT_URL = 'student-home'
# LOGIN_URL = 'login'
