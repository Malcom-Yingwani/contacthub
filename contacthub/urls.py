from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from django.http import HttpResponse


urlpatterns = [path("admin/", admin.site.urls), path("", include("contacts.urls"))]


def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "YourPassword123")
        return HttpResponse("Admin created!")
    return HttpResponse("Admin already exists")
