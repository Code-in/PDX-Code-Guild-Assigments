from django.db import models

# Create your models here.

def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return '{0}_{1}'.format(instance.id, filename) 

class SupportType(models.Model):
    support_type = models.CharField(max_length=32)

    def __str__(self):
        return f"ID:{self.id} Type:{self.support_type}"

class Support(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=128)
    title = models.CharField(max_length=128)
    message = models.TextField(max_length=1024)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    iphone = models.CharField(max_length=48)
    ios = models.CharField(max_length=16)
    prior_support_id = models.IntegerField(blank=True, null=True)
    response = models.ForeignKey(SupportType, on_delete=models.CASCADE, related_name="support", blank=True, null=True)
    responsed_too = models.BooleanField(default=False)
    def __str__(self):
        return f"ID:{self.id} Title:{self.title[:25]} Prior Support ID:{self.prior_support_id} "

