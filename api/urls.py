from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UsersToolsForAdminViewSet, UserProfileChangeViewSet


router = DefaultRouter()
router.register('users', UsersToolsForAdminViewSet)
    
urlpatterns = [
    #path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('v1/', include('drfpasswordless.urls')),
    path('v1/users/me/', UserProfileChangeViewSet.as_view()),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(router.urls)),
]
