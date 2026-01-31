from django.shortcuts import render


# Create your views here.
from .models import Projects,Tasks

from django.http import JsonResponse
import json


def create_project(request):
    
    if request.method !="POST":
        return JsonResponse({"error":"method not allowed"},status=405)

    try:
        data= json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "invalid json"}, status=400)
    if Projects.objects.filter(name=data.get('name')).first():
        return JsonResponse({"error":"project name already exists"},status=401)

    new_project= Projects(owner=request.user,name=data.get('name'),description=data.get('description'))
    new_project.save()
    return JsonResponse({"message":"created succesfully"},status=201)

    
    


def get_project(request):
    if request.method !="GET":
        return JsonResponse({"error":"method not allowed"},status=405)
    
    projects= Projects.objects.filter(owner=request.user)

    data= []
    for project in projects:
        data.append({
            "id":project.id,
            "name": project.name,
            "description" : project.description,
            "created_at":project.created_at


        })



    

    return JsonResponse({"message":data},status=200)
    


def create_task(request,project_id):
    if request.method !="POST":
        return JsonResponse({"error":"method not allowed"},status=405)
    
    try:
        data= json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "invalid json"}, status=400)
    project= Projects.objects.filter(id=project_id).first()
    
    new_task = Tasks(project=project,title=data.get('title'))
    new_task.save()

    
   

    
    return JsonResponse({"message":"task created successfully"},status=201) 




def get_tasks(request,project_id):
    if request.method!="GET":
        return JsonResponse({"error:":"method not allowed"},status=405)


    project= Projects.objects.filter(id=project_id).first()

    if not project:
        return JsonResponse({"error":"project does not exist in database"},status=400)

    
    tasks= Tasks.objects.filter(project=project)


    data= []

    for task in tasks:

        data.append({
            "id":task.id,
            "title":task.title,
            "compeleted":task.compeleted,
            "created_at":task.created_at


        })

    return JsonResponse({"message":data},status=200)




def mark_tasks(request,task_id):
    if request.method != "PATCH":
        return JsonResponse({"error":"method not allowed"},status=405)
    
    task = Tasks.objects.filter(id=task_id).first()
    if not task:
        return JsonResponse({"error":"task not in database"},status=400)
    
    task.compeleted= not task.compeleted
    task.save()

    return JsonResponse({"message":"patched successfully"},status=200)

def delete_projects(request,project_id):
    if request.method != "DELETE":
        return JsonResponse({"error":"method not allowed"},status=405)
    
    project=Projects.objects.filter(id=project_id).first()

    project.delete()

    return JsonResponse({"message":"successfully deleted"},status=200)