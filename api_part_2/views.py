from rest_framework import viewsets, exceptions, filters, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly, AdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ViewSetMixin


class TitleView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('name', 'year', 'genre', 'category', )

    def perform_create(self, serializer):
        serializer.save()

class GenreView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, AdminOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'slug']

class CategoryView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, AdminOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'slug']
