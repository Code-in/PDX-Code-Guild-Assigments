from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.core.paginator import Paginator
from django.urls import reverse
# from django import template

# register = template.Library()




# Create your views here.

PAGECOUNT = 12

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
        "pokemon_per_page": PAGECOUNT
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

# @register.filter
# def modulo(num, val):
#     return num % val

# @register.filter(name='tim')
# def times(value, arg):
#     "Multiplies the arg and the value"
#     return int(value) * int(arg)

# @register.filter(name='sub')
# def subtraction(value, arg):
#     "Subtracts the arg from the value"
#     return int(value) - int(arg)

# @register.filter(name='div')
# def divison(value, arg):
#     "Divides the value by the arg"
#     return int(value) / int(arg)

# @register.filter(name='cei')
# def compute_exact_id(value, rb_page_no):    
#     new_id = value+(5*(rb_page_no-1))    ## here's the mathematical operation
#     return new_id