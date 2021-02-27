from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.

def index(request):

    blog_posts = BlogPost.objects.all()

    context = {
        "blog_posts" : blog_posts
    }
    #return HttpResponse('Hello World!')
    return render(request, 'myapp/index.html', context)
