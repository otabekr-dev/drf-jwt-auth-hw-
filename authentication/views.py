from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from auth_service import GoogleAuthService
from accounts.permissions import IsAdmin, IsManager, IsUser

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated, IsUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request) -> Response:
        return Response({'message': 'hello user'})
    
class AdminProfileView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request) -> Response:
        return Response({'message': 'hello admin'})
    
class ManagerProfileView(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    authentication_classes = [JWTAuthentication]    


class GoogleLoginView(APIView):

    def post(self, request: Request) -> Response:
        url = GoogleAuthService.generate_google_url()
        return Response(
            {
                'message': 'link to login by google',
                'google_auth_link': url
            }
        )
    

class GoogleCallbackView(APIView):

    def get(self, request: Request) -> Response:
        code = request.query_params.get('code')
        if code is None:
            return Response({'error': 'code is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        tokens = GoogleAuthService.login_by_google(code)
        return Response({'tokens': tokens})