from django.urls import path

from .views import Home,contact,about

urlpatterns = [
    path("",Home),
    path("contact/",contact),
    path("about/",about)
]
