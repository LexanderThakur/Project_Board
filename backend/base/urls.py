from django.urls import path
from . import views
urlpatterns=[
    path("create/",views.create_project),
    path("get_project/",views.get_project),
    path("create_task/<int:project_id>/",views.create_task),
    path("get_tasks/<int:project_id>/",views.get_tasks),
        
]