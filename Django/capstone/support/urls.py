from django.urls import path
from . import views


app_name = 'support'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkin/', views.checkin, name="checkin"),
    path('request/', views.response, name='request'),
    path('datatable/', views.datatable, name='datatable'),
    path('response/<int:id>/', views.response, name="response"),
] 

