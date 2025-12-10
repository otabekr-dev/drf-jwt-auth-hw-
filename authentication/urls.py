from django.urls import path
from rest_framework_simplejwt import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserProfileView, AdminProfileView, ManagerProfileView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserProfileView.as_view(), name='user-view'),
    path('admin/', AdminProfileView.as_view(), name='admin-view'),
    path('manager/', ManagerProfileView.as_view(), name='manager-view')
]

