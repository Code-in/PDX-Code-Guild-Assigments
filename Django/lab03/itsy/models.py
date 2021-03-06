from django.db import models

# Create your models here.

class Itsy(models.Model):
    code = models.CharField(max_length=128)
    url = models.URLField(max_length=1024)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}) {self.code[:16]} Count: {self.count} --> {self.url[:128]}"