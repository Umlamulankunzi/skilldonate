"""
URL configuration for skilldonate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index, how_it_works, about, contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path("charities/", include("charities.urls")),
    path("volunteers/", include("volunteers.urls")),
    path("skills/", include("skills.urls")),
    path("search/", include("search.urls")),
    path("skilldonate-auth/", include("app_auth.urls")),
    path("", index, name='home'),
    path("how-it-works", how_it_works, name='how-it-works'),
    path("about", about, name='about'),
    path("contact", contact, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
