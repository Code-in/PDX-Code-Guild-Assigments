from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .models import Support, SupportType
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

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

        obj, created = SupportType.objects.get_or_create(support_type='support')
        obj.save()

        support.response = obj
        support.prior_support_id=last_id
        support.save()

        print("Success Posting")
        
        return HttpResponseRedirect(reverse('support:index'))  # TODO: Need to redirect to another page and tell them we'll get back them as soon as possible
    return render(request, 'support/index.html')
    #print("No POST")
    #return HttpResponse("Hello, world. You're at the Support-App index.")

def request(request):
    if request.user.is_authenticated:
        print("Success authenticated")
        support = Support.objects.all()

        context = {
            "support": support,
        }
        return render(request, 'support/response.html', context)
    print("Failure NOT authenticated")
    return render(request, 'support/index.html')





def response(request, id):
    print("Got here!")
    if request.user.is_authenticated:
        if request.method == "POST":
            support = Support.objects.get(id=id)
            form = request.POST
            msg = form['msg']
            print("Success Posting")
            send_mail(
                'RE:>' + support.title,
                msg,
                settings.SUPPORT_EMAIL,
                [support.email],
                fail_silently=False,
            )

            return HttpResponseRedirect(reverse('support:index'))
        else:
            # TODO: Need to fill out a single page details via context
            return render(request, 'support/response.html')
    return render(request, 'support/index.html')




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
