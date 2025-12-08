from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search_contacts, name="search"),
    path("create/", views.create_contact, name="create-contact"),
    path("delete<int:pk>/", views.delete_contact, name="delete-contact"),
    path(
        "contacts/<int:pk>/download/", views.download_document, name="download-document"
    ),
]
