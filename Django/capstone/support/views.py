from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the Support-App index.")

def index(request):
    print("Got here!")
    if request.method == "POST":
        # form = request.POST
        # title = form['title']
        # body = form['body']
        # image = request.FILES.get('image', '')

        # blog = BlogPost()
        # blog.title = title
        # blog.body = body
        # if image:
        #     blog.image = image

        # user = User.objects.get(id=request.user.id)
        # blog.user = user
        # blog.save()
        print("Success Posting")
        return HttpResponse("We POSTed. You're at the Support-App index.")
        #return HttpResponseRedirect(reverse('profile'))
    return render(request, 'support/index.html')
    #print("No POST")
    #return HttpResponse("Hello, world. You're at the Support-App index.")