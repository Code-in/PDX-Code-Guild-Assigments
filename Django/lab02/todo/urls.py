from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('remove/<int:id>/', views.remove, name="remove"),
    path('completed/<int:id>/', views.completed, name="completed"),
]