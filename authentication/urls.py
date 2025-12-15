from django.urls import path
from rest_framework_simplejwt import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    UserProfileView,
    AdminProfileView,
    ManagerProfileView, GoogleLoginView,
    GoogleCallbackView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserProfileView.as_view(), name='user_view'),
    path('admin/', AdminProfileView.as_view(), name='admin_view'),
    path('manager/', ManagerProfileView.as_view(), name='manager_view'),
    path('google/login/', GoogleLoginView.as_view(), name='google_login'),
    path('google/callback/', GoogleCallbackView.as_view(), name='google_login')
]

