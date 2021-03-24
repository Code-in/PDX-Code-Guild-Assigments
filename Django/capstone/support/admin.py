from django.contrib import admin
from .models import Support, SupportType


# Register your models here.
admin.site.register(SupportType)
admin.site.register(Support)


