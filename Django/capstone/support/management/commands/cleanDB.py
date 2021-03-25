from django.core.management.base import BaseCommand
from support.models import Support, SupportType
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import json


# Manage.py command which allows me to import basic support data for testing.

class Command(BaseCommand):

    def handle(self, *args, **options):
        Support.objects.all().delete()
        SupportType.objects.all().delete()


