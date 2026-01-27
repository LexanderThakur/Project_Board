from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
# Create your views here.
from .models import Projects,Tasks
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    ProjectCreateSerializer,
    TaskCreateSerializer,
    ProjectSerializer,
    TaskSerializer
)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_project(request):
    
    data=request.data

    serializer= ProjectCreateSerializer(data=data)
    
    serializer.is_valid(raise_exception=True)
    serializer.save(owner=request.user)
    return Response({"message":"created succesfully","data":serializer.data},status=201)

    
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_project(request):
    
    
    project= Projects.objects.filter(owner=request.user)

    serializer= ProjectSerializer(project,many=True)

    return Response({"message":serializer.data},status=200)
    


    