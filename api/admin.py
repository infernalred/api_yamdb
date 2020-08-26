from django.contrib import admin

from .models import Review, Comment


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "text", "author", "score", "pub_date")
    search_fields = ("text",)
    list_filter = ("pub_date", "title",)
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "review", "text", "author", "pub_date")
    search_fields = ("text",)
    list_filter = ("pub_date", "author", "review",)
    empty_value_display = "-пусто-"
