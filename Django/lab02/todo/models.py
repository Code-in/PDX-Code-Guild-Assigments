from django.db import models

#Add a Priority model with a name field (e.g. low, medium, high). 
# Then add a ForeignKeyField to the TodoItem linking it to a Priority. 
# The form for creating a todo item should also have a dropdown list for 
# selecting the priority. Display the priority in the list of todo items.

class Priority(models.Model):
    state = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.state}"

# Create your models here.
# This can be done with a single model TodoItem which contains a CharField description, 
# a DateTimeField created_date, a nullable DateTimeField completed_date. 
# Newly created TodoItems should have a null completed date. 

class TodoItem(models.Model):
    todo_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True, default=None)
    priority = models.ForeignKey(Priority, default=2, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id}) {self.todo_description[:25]}... {self.created_date}"




