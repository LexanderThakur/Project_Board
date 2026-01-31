
import jwt
from django.conf import settings
from accounts.models import User
from django.http import JsonResponse
class JWTMiddleware:

    def __init__(self,get_response):
        self.get_response=get_response
        self.public_paths=['/','/auth/login/','/auth/register/','/favicon.ico']
        
    def __call__(self,request):
        

        if request.method=='OPTIONS':
            return self.get_response(request)
        
        
        if request.path.startswith("/static/") or request.path.startswith('/.well-known/'):
            return self.get_response(request)
        
        if request.path in self.public_paths :
            return self.get_response(request)
        
     

        jwt_token= request.COOKIES.get("jwt")


        if not jwt_token:
            return JsonResponse({"error":"token missing please login again"},status=401)

        try:

            payload= jwt.decode(jwt_token,settings.JWT_SECRET,algorithms=["HS256"])
            user_id = payload.get("user_id")

            if not user_id:
                return JsonResponse({"error": "invalid token payload"}, status=401)
            user=User.objects.filter(id=user_id).first()
            if not user:
                return JsonResponse({"error":"user not found"},status=401   )

            request.user=user
            


        except jwt.exceptions.ExpiredSignatureError:

            return JsonResponse({"error":"token expired login again"},status=401)
        except jwt.exceptions.InvalidTokenError:
            return JsonResponse({"error":"token failed please login again"},status=401)
            
        return self.get_response(request)



        