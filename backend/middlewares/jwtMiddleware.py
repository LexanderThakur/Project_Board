
import jwt
class JWTMiddleware:

    def __init__(self,get_response):
        self.get_response=get_response
        self.public_paths=['/','/login/','/register/','/favicon.ico/','/static/',"/.well-known/"]
        
    def __call__(self,request):
        if request.path in self.public_paths or request.method=='OPTIONS':
            return self.get_response(request)
        

        