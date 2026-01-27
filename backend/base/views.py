from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from models import Projects,Tasks


@api_view(["POST"])
def create_project(request):
    user= request.user

    if not user:
        return Response({"error":"please log in first"},status=401)
    
    data=request.data

    project_name=data.get("name",None)
    project_description=data.get("description",None)
    if not project_name or project_description:
        return Response({"error":"Project name and description must not be null"},status=401)

    if Projects.objects.filter(project_name=project_name).first():
        return Response({"error":"Project already exists"},status=401)

    new_project= Projects(
        owner=user,
        name=project_name,
        description=project_description,

    )
    new_project.save()
    return Response({"message":"project created succesfully"},status=201)