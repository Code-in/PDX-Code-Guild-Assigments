import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import BlogPost

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("index")

def register(request):
    if request.method == "GET":
        error = request.GET.get("error", "")
        username = request.GET.get("username", "")
        email = request.GET.get("email", "")
        context = {
            'error': error,
            'username': username,
            'email': email
        }
        return render(request, 'blog/register.html', context)

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        email = request.POST['email']

        if password == confirm:
            User.objects.create_user(username, email, password)
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('register') + f'?error=passwords do not match&username={username}&email={email}')


def user_login(request):
    if request.method == "GET":
        error = request.GET.get('error', '')
        context = {
            'error': error
        }
        return render(request, 'blog/login.html', context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print("Who's the user", user)
        if user is not None:
            login(request, user)
            # Redirect to success...
            print("Redirect to success...")
            return HttpResponseRedirect(reverse('index'))
        else:
            print("or here?")
            return HttpResponseRedirect(reverse('login') + '?error=Username or Password is incorrect.')
    #return HttpResponse("login")

def profile(request):
    if request.user.is_authenticated:
        blogs = BlogPost.objects.filter(user=request.user)
        context = {
            'blogs': blogs,
            'user': request.user
        }
        return render(request, 'blog/profile.html', context)
        
    else:
        return HttpResponseRedirect(reverse('register'))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def delete_blog(request, id):
    blog = BlogPost.objects.get(id=id)
    if blog.user == request.user:
        blog.delete()
    return HttpResponseRedirect(reverse('profile'))

def update_blog(request, id):
    if request.method == "GET":
        blog = BlogPost.objects.get(id=id)
        if blog.user == request.user:
            context = {
                'blog': blog,
                'user': request.user
            }
            return render(request, 'blog/update.html', context)
        else:
            return HttpResponseRedirect(reverse('index'))
    elif request.method == "POST":
        blog = BlogPost.objects.get(id=id)
        if blog.user == request.user:
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            return HttpResponseRedirect(reverse('index'))


def posts(request):
    blogs = BlogPost.objects.filter(public=True)
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/posts.html', context)

def details(request, id):
    blog = BlogPost.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/details.html', context)


def create_blog(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = request.POST
        title = form['title']
        body = form['body']
        image = request.FILES.get('image', '')

        blog = BlogPost()
        blog.title = title
        blog.body = body
        if image:
            blog.image = image

        user = User.objects.get(id=request.user.id)
        blog.user = user
        blog.save()
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'blog/create.html')