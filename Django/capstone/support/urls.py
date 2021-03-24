from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'support'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkin/', views.checkin, name="checkin"),
    path('response/', views.response, name='response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)