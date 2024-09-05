from django.contrib import admin
from .models import ProfileModel, OTPModel
# Register your models here.
@admin.register(ProfileModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['user']

@admin.register(OTPModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['user', 'otp']