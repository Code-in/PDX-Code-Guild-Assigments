from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.

PAGECOUNT = 60

def index(request):
    pokemon = Pokemon.objects.all()
    pokemon_type = PokemonType.objects.all()
    pokinator = Paginator(pokemon, PAGECOUNT)
    page = request.GET.get('page')
    pokepage = pokinator.get_page(page)
    print(pokemon)
    context = {
        "pokemon": pokepage,
        "pokemon_type": pokemon_type,
        "count": PAGECOUNT
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

   # {%url 'pokedex:index'%}