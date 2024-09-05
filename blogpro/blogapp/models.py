from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    title=models.CharField( max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date_created=models.DateTimeField( auto_now_add=False)

    class Meta:
        ordering = ['-date_created']

    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()


    def __str__(self):
        return self.title
    
    

class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="comment_set")
    content=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.content
    
    