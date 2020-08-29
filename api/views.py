from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, permissions, filters, status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination

from .models import CustomUser
from .serializers import UserForAdminSerializer, UserSerializer


class UsersToolsForAdminViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserForAdminSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'username'
    filter_backends = [filters.SearchFilter]
    search_fields = ['=username']
    pagination_class = PageNumberPagination


class UserProfileChangeViewSet(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        print(self.request.user.email)
        obj = get_object_or_404(CustomUser, email=self.request.user.email)
        print(obj.email)
        return obj
