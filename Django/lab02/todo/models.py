from django.db import models

# Create your models here.
# This can be done with a single model TodoItem which contains a CharField description, 
# a DateTimeField created_date, a nullable DateTimeField completed_date. 
# Newly created TodoItems should have a null completed date. 

class TodoItem(models.Model):
    todo_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}) {self.todo_description[:25]}... {self.created_date}"