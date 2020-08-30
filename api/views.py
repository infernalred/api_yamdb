from rest_framework import viewsets, filters, status, permissions
from rest_framework.generics import get_object_or_404, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Review, Title, Genre, Category, Comment, CustomUser
from api.permissions import IsAdminOrReadOnly, IsAuthorOrModerator, IsAdminUser, AdminOrReadOnly
from api.serializers import CommentSerializer, ReviewSerializer, \
    TitleSerializer, GenreSerializer, CategorySerializer, \
    UserForAdminSerializer, UserSerializer


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


class TitleView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'year', 'genre', 'category',)

    # def perform_create(self, serializer):
    #     name = self.request.data.get('name')
    #     year = self.request.data.get('year') or None
    #     description = self.request.data.get('description') or None
    #     category_slug = self.request.data.get('category') or None
    #     genre_slug = self.request.data.get("genre") or None
    #     if genre_slug is not None:
    #         if len(genre_slug)>1:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #         genre = get_object_or_404(Genre, slug=genre_slug[0])
    #         genres = []
    #         genres.append(genre)
    #     else:
    #         genres = []
    #     if category_slug is not None:
    #         category = get_object_or_404(Category, slug=category_slug)
    #     else:
    #         category = None
    #     if serializer.is_valid:
    #             serializer.save(name=name, category=category, genre=genres, year=year, description=description)

    def perform_update(self, serializer):
        category_slug = self.request.data.get('category')
        category = get_object_or_404(Category, slug=category_slug)
        genre_slugs = self.request.data.get('genre')
        genres = []
        for genre_slug in genre_slugs:
            genre = get_object_or_404(Genre, slug=genre_slug)
            genres.append(genre)
        if serializer.is_valid():
            serializer.save(category=category, genre=genres)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class GenreView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoryView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly|IsAuthorOrModerator&IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title.objects, pk=title_id)
        queryset = title.reviews.all()
        return queryset

    def create(self, request, *args, **kwargs):
        title_id = self.kwargs.get("title_id")
        user = request.user
        title = get_object_or_404(Title.objects, pk=title_id)
        if Review.objects.filter(title=title, author=user).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=user, title=title)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly|IsAuthorOrModerator&IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        title = get_object_or_404(Title.objects, pk=title_id)
        review = get_object_or_404(Review.objects, pk=review_id)
        queryset = Comment.objects.filter(title=title, review=review).all()
        return queryset

    def perform_create(self, serializer):
        """Create a new comment."""
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        title = get_object_or_404(Title.objects, pk=title_id)
        review = get_object_or_404(Review.objects, pk=review_id)
        serializer.save(author=self.request.user, title=title,
                        review=review)
