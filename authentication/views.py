from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

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