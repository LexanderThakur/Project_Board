from django.urls import path
from . import views
urlpatterns=[
    path("create/",views.create_project),
    path("get_project/",views.get_project),
]