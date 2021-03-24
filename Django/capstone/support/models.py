from django.db import models

# Create your models here.

def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'images/email_{0}/{1}'.format(instance.email, filename) 


class SupportType(models.Model):
    support_type = models.CharField(max_length=32)
    support_id = models.IntegerField(blank=False)

    def __str__(self):
        return f"ID:{self.id} Type:{self.support_type} Prior Support ID:{self.support_id}"

class Support(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=128)
    title = models.CharField(max_length=128)
    message = models.TextField(max_length=1024)
    image = models.ImageField(upload_to=user_directory_path, default = None)
    iphone = models.CharField(max_length=48)
    ios = models.CharField(max_length=16)
    response = models.ForeignKey(SupportType, on_delete=models.CASCADE, related_name="support", blank=True, null=True)

    def __str__(self):
        return f"ID:{self.id} Title:{self.title[:25]}"

