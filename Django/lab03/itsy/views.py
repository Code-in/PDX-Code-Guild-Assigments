from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Itsy
import string
import random

CODE_LENGTH = 6
# Create your views here.

def index(request):
    urls = Itsy.objects.order_by("-count")
    context = {
        "urls": urls,
    }
    return render(request, 'itsy/index.html', context)


def save(request):
    form = request.POST
    itsy = Itsy()
    itsy.url = form['url'] 
    itsy.code = create_random_code(CODE_LENGTH)   
    itsy.save()
    return HttpResponseRedirect(reverse('index'))

def proxy(request, slug):
    #itsy = Itsy.objects.get(code=slug)
    itsy = get_object_or_404(Itsy, code=slug)
    itsy.count += 1
    itsy.save()
    return HttpResponseRedirect(itsy.url)


# Create the character pool for the random generation of passwords
chars = string.ascii_letters + string.digits

# Create the random password per the length requested
def create_random_code(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(chars)
    return pwd