from django.core.management.base import BaseCommand
from support.models import Support, SupportType
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import json


# Manage.py command which allows me to import basic support data for testing.

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./support/management/commands/support.json', 'r') as file:
            raw_text = file.read()
        support_data = json.loads(raw_text)

        print(support_data)

        Support.objects.all().delete()
        SupportType.objects.all().delete()

        for data in support_data:
            print(data)
            sticket = Support()
 
            sticket.email = data['email']
            sticket.title = data['title']
            sticket.message = data['message']
            if not data['image'] == None:
                sticket.image = data['image']
            sticket.iphone = data['iphone']
            sticket.ios = data['ios']

            sticket.prior_support_id=data['prior_support_id']
            sticket.save()

            if not data['response'] == None:
                st_obj, created = SupportType.objects.get_or_create(support_type=data['response']['support_type'])

            print(st_obj)
            sticket.response = st_obj
            sticket.save()
