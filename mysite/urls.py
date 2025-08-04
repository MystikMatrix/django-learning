from django.contrib import admin
from django.urls import include, path
from dwitter import views

urlpatterns = [
    path("polls/", include("polls.urls")), 
    path("admin/", admin.site.urls),
    path('', views.home),
]