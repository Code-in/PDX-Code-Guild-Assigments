from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.urls import reverse
# Create your views here.

def index(request):
    pokemon = Pokemon.objects.all()
    pokemon_type = PokemonType.objects.all()
    print(pokemon)
    context = {
        "pokemon": pokemon,
        "pokemon_type": pokemon_type,
        "loop_times": range(1, 12)
    }
    return render(request, 'pokedex/index.html', context)

def pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    pokemon_type = PokemonType.objects.all()
    print(pokemon)
    context = {
        "pokemon": pokemon,
        "pokemon_type": pokemon_type,
    }
    return render(request, 'pokedex/pokemon.html', context)