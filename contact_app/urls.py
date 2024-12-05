from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("Dashbord/", views.index, name="dashbord"),
    path("", views.login, name="login"),
    path("add_task/", views.add_task, name="add_task"),
    path("crud/", views.crud, name="crud"),
    path("update/<int:task_id>/", views.update, name="update"),
    path("search/", views.search, name="search"),
    path("contacts/", views.contacts, name="contacts"),
    path("logout/", views.logout, name="logout"),
    path("setting/", views.setting, name="setting"),
    path("card/<int:contact_id>/<str:type>/", views.card, name="card"),
    path("add_contact/", views.add_contact, name="add_contact"),
    path("crud_contact/", views.crud_contact, name="crud_contact"),
    path("update_contact/<int:contact_id>/", views.update_contact, name="update_contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)