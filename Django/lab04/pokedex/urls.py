from django.urls import path

from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<int:id>/', views.pokemon, name="pokemon"),
]