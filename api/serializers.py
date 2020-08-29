from django.db.models import Avg
from rest_framework import serializers

from .models import Comment, Review, Title, \
    Category, Genre, CustomUser


class UserForAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", 
                  "bio", "email", "role")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", 
                  "bio", "email", "role")
        read_only_fields = ("role", "email")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "name", "year", "genre", "rating", 
                  "category", "description")
        read_only_fields = ("id", )
        model = Title

    def get_rating(self, obj):
        rating = obj.reviews.all().aggregate(Avg("score")).get("score__avg")
        if rating is None:
            return 0
        return rating


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "score", "pub_date",)
        read_only_fields = ("id", "author", "pub_date")
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "pub_date",)
        read_only_fields = ("id", "author", "pub_date",)
        model = Comment
