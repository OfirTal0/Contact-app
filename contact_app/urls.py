from django.urls import path
from . import views


urlpatterns = [
    path("Dashbord/", views.index, name="dashbord"),
    path("", views.login, name="login"),
    path("add_contact/", views.add_contact, name="add_contact"),
    path("crud/", views.crud, name="crud"),
    path("update/<int:contact_id>/", views.update, name="update"),
    path("search/", views.search, name="search"),
    path("groups/", views.groups, name="groups"),
    path("logout/", views.logout, name="logout"),
]