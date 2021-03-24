from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .models import Support, SupportType
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the Support-App index.")

def index(request):
    print("Got here!")
    if request.method == "POST":
        support = Support()
        form = request.POST
        support.title = form['title']
        support.email = form['email']
        support.message = form['message']
        support.image = request.FILES.get('image', '')
        support.iphone = form['iphone']
        support.ios = form['ios']

        priors = Support.objects.filter(email=support.email)
        last_id = 0
        for prior in priors:
            print(f"Prior email: {last_id}")
            if prior.id > last_id and prior.response.support_type == "support":
                last_id = prior.id 
                print(f"Last: {last_id}")

        obj, created = SupportType.objects.get_or_create(support_type='support', support_id=last_id)
        obj.save()

        support.response = obj
        support.save()

        print("Success Posting")
        return HttpResponse("We POSTed. You're at the Support-App index.")
        #return HttpResponseRedirect(reverse('profile'))
    return render(request, 'support/index.html')
    #print("No POST")
    #return HttpResponse("Hello, world. You're at the Support-App index.")

def response(request):
    if request.user.is_authenticated:
        print("Success authenticated")
        return render(request, 'support/response.html')
    print("Failure NOT authenticated")
    return render(request, 'index.html')


def checkin(request):
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']
        user = authenticate(request, username=username, password=password)
        print(username, password, user)
        if user is not None:
            print('logging in user')
            login(request, user)
            return HttpResponseRedirect(reverse('support:response'))
    return render(request, 'support/checkin.html')



# def user_login(request):
#     if request.method == "GET":
#         error = request.GET.get('error', '')
#         context = {
#             'error': error
#         }
#         return render(request, 'support/login.html', context)
#     elif request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
#         print("Who's the user", user)
#         if user is not None:
#             login(request, user)
#             # Redirect to success...
#             print("Redirect to success...")
#             print("Success authenticated")
#             return render(request, 'support/response.html')
#         else:
#             print("Error or here?")
#             return HttpResponseRedirect(reverse('support:login') + '?error=Username or Password is incorrect.')
#     print("Neither POST or GET")
#     return render(request, 'support/index.html')
