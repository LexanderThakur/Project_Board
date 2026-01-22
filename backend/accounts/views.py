
from rest_framework.response import Response 
from rest_framework.decorators import api_view
import json

from django.contrib.auth.hashers import make_password,check_password
from accounts.models import User
import jwt
import datetime
from django.conf import settings



@api_view(['POST'])
def login(request):
    data= request.data

    user_email=data.get('user_email',None)
    user_password= data.get('user_password',None)
    
    user= User.objects.filter(user_email=user_email).first()
    if not user:
        return Response({'error':'user does not exist'})
    if not check_password(user_password,user.user_password):
        return Response({'error':'invalid password'})
    
    payload={
        'user_id':user.id,
        'user_email':user.user_email,
        'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=30),
        "iat": datetime.datetime.utcnow(),

    }
    

    encoded_jwt= jwt.encode(payload,settings.JWT_SECRET,algorithm='HS256')
    response=Response({"message":"successfully logged in"},status=200)

    response.set_cookie(
        key='jwt',
        value=encoded_jwt,
        httponly=True,
        secure=False,
        samesite='Lax',
        path='/'

    )
    return response




@api_view(['POST'])
def register(request):
    data= request.data

    user_email=data.get('user_email',None)
    user_password= data.get('user_password',None)
    
    user= User.objects.filter(user_email=user_email).first()
    if  user:
        return Response({'error':'user already exists'})
    user= User(user_email=user_email,user_password=make_password(user_password))
    user.save()
    payload={
        'user_id':user.id,
        'user_email':user.user_email,
        'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=30),
        "iat": datetime.datetime.utcnow(),
    }
    

    encoded_jwt= jwt.encode(payload,settings.JWT_SECRET,algorithm='HS256')
    response=Response({"message":"successfully registered"},status=200)

    response.set_cookie(
        key='jwt',  
        value=encoded_jwt,
        httponly=True,
        secure=False,
        samesite='Lax',
        path='/ '

    )
    return response