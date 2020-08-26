from django.contrib import admin
from .models import *


class TitleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year", "genre", "category") 
    search_fields = ("name",) 
    list_filter = ("name",) 
    empty_value_display = "-пусто-" 

class GenreAdmin(admin.ModelAdmin):
    list_display = ("id","name","slug")
    search_fields = ("name",) 
    list_filter = ("name",) 
    empty_value_display = "-пусто-" 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","slug")
    search_fields = ("name",) 
    list_filter = ("name",) 
    empty_value_display = "-пусто-"        




admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)