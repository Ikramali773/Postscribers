from django.contrib import admin
from .models import PostModel, Comments
# Register your models here.
@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['title', 'date_created']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['user', 'content']


