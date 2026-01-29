from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
# Create your views here.
from .models import Projects,Tasks
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import (
    ProjectCreateSerializer,
    TaskCreateSerializer,
    ProjectSerializer,
    TaskSerializer
)

def auth_error(request):
    if not request.user:
        return JsonResponse({"error":"user not logged in"},status=401)


@api_view(["POST"])
def create_project(request):
    
    data=request.data

    serializer= ProjectCreateSerializer(data=data)
    
    serializer.is_valid(raise_exception=True)
    serializer.save(owner=request.user)
    return Response({"message":"created succesfully","data":serializer.data},status=201)

    
    

@api_view(["GET"])
def get_project(request):
    
    
    project= Projects.objects.filter(owner=request.user).first()

    serializer= ProjectSerializer(project,many=True)

    return Response({"message":serializer.data},status=200)
    

@api_view(["POST"])
def create_task(request,project_id):
    
    project= Projects.objects.filter(id=project_id)


    
   

    serializer= TaskCreateSerializer(data=request.data)   
    serializer.is_valid(raise_exception=True)
    serializer.save(project=project)
    return Response({"message":"task created successfully"},status=201) 