from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to=user_directory_path, default = None)
    public = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogposts", blank=True, null=True)
    # (optional) date_edited (DateTimeField with auto_now=True)
    
    def __str__(self):
        return f"{self.id}) {self.title[:25]}..."
