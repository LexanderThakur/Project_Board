

import json

from django.contrib.auth.hashers import make_password,check_password
from accounts.models import User
import jwt
import datetime
from django.conf import settings

from django.http import JsonResponse





def me(request):
    if request.method !="GET":
        return JsonResponse({"error":"method not allowed"},status=405)
    user= request.user
    if not user:
        return JsonResponse({"error":"user not found "},status=401)
    


    user_email= user.user_email
    return JsonResponse({"user_email":user_email},status=200)




def login(request):
    try:
        data= json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "invalid json"}, status=400)

    user_email=data.get('user_email',None)
    user_password= data.get('user_password',None)
    
    user= User.objects.filter(user_email=user_email).first()
    if not user:
        return JsonResponse({'error':'user does not exist'},status=404)
    if not check_password(user_password,user.user_password):
        return JsonResponse({'error':'invalid password'})
    
    payload={
        'user_id':user.id,
        'user_email':user.user_email,
        'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=30),
        "iat": datetime.datetime.utcnow(),

    }
    

    encoded_jwt= jwt.encode(payload,settings.JWT_SECRET,algorithm='HS256')
    response=JsonResponse({"message":"successfully logged in"},status=200)

    response.set_cookie(
        key='jwt',
        value=encoded_jwt,
        httponly=True,
        secure=False,
        samesite='Lax',
        path='/'

    )
    return response





def register(request):
    try:
        data= json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "invalid json"}, status=400)

    user_email=data.get('user_email',None)
    user_password= data.get('user_password',None)
    
    user= User.objects.filter(user_email=user_email).first()
    if  user:
        return JsonResponse({'error':'user already exists'},status=409)
    user= User(user_email=user_email,user_password=make_password(user_password))
    user.save()
    payload={
        'user_id':user.id,
        'user_email':user.user_email,
        'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=30),
        "iat": datetime.datetime.utcnow(),
    }
    

    encoded_jwt= jwt.encode(payload,settings.JWT_SECRET,algorithm='HS256')
    response=JsonResponse({"message":"successfully registered"},status=200)

    response.set_cookie(
        key='jwt',  
        value=encoded_jwt,
        httponly=True,
        secure=False,
        samesite='Lax',
        path='/'

    )
    return response