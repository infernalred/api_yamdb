from rest_framework import serializers

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "score", "pub_date",)
        read_only_fields = ("id", "author", "pub_date")
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(slug_field="title_id",
                                         read_only=True)
    review = serializers.SlugRelatedField(slug_field="review_id",
                                          read_only=True)
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "pub_date",)
        read_only_fields = ("author", "pub_date",)
        model = Comment
