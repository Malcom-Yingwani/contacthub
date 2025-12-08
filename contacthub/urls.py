from django.contrib import admin
from django.urls import include, path
from contacts.views import create_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("contacts.urls")),
    path("create_admin/", create_admin),
]
