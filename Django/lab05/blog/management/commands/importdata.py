from django.core.management.base import BaseCommand
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./blog/management/commands/data.json', 'r') as file:
            raw_text = file.read()
        blogs = json.loads(raw_text)

        BlogPost.objects.all().delete()

        user = User.objects.get(username='pparks')
        print(user)
            
        for blog in blogs:
            print(blog)
            blog_post = BlogPost()
            blog_post.title = blog['title']
            blog_post.body = blog['body']
            blog_post.public = True
            blog_post.save()

            # if blog['userId']:
            #     user, created = User.objects.get_or_create(id=blog['userId'])

            blog_post.user = user
            blog_post.save()

