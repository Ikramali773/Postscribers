from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from datetime import datetime
# Create your models here.
class ProfileModel(models.Model):
    user=models.OneToOneField(User,  on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile', validators=[FileExtensionValidator(['png','jpg'])])

    def __str__(self) :
        return self.user.username   

class OTPModel(models.Model):
     user=models.OneToOneField(User,  on_delete=models.CASCADE,)
     otp=models.IntegerField(null=True)
     otp_time=models.DateTimeField(auto_now_add=False, default=datetime.now())