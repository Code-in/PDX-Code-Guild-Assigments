from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.utils import timezone
from .models import TodoItem

# The index page should have a list of all the todo items (showing only the name), 
# with completed items in a separate list (or at the bottom of the existing list) 
# with grey color and maybe a line through them. There should also be a text field 
# and a button (in a form), When the clicks the button it should saves a new todo item 
# to the database and shows the newly-added item in the list. Use one view to render 
# the template, and another view to receive the form submission and redirect back 
# to the first view.


# Create your views here.
def index(request):
    return HttpResponse("made it to todo index")

def index(request):
    todos = TodoItem.objects.order_by('-created_date')[:20]
    context = {
        "todos": todos
    }
    return render(request, 'todo/index.html', context)

def post(request):
    form = request.POST
    todo = TodoItem()
    todo.todo_description = form['todo_description']
    todo.save()
    return HttpResponseRedirect(reverse('index'))

def remove(request, id):
    todo = TodoItem.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

def completed(request, id):
    todo = TodoItem.objects.get(id=id)
    todo.completed_date = timezone.now()
    todo.save()
    return HttpResponseRedirect(reverse('index'))