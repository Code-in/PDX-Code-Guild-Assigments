from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
from django.shortcuts import get_object_or_404
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            raw_text = file.read()
        pjson = json.loads(raw_text)

        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()

        pokemons = pjson["pokemon"]


        for pokemon in pokemons:
            ptypes = pokemon['types']
            print(ptypes)
            for ptype in ptypes:
                print(ptype)
                if PokemonType.objects.filter(name=ptype):
                    print("Already exsist")
                else:
                    print("Creating a new type")
                    pokemontype = PokemonType()
                    pokemontype.name = ptype
                    pokemontype.save()
            

        for pokemon in pokemons:
            poke = Pokemon()
            poke.number = pokemon['number']
            poke.name = pokemon['name']
            poke.height = pokemon['height']
            poke.weight = pokemon['weight']
            poke.image_front = pokemon['image_front']
            poke.image_back = pokemon['image_back']
            ptypes = pokemon['types']
            poke.save()
            print(ptypes)
            for ptype in ptypes:
                pokeType = PokemonType.objects.get(name=ptype)
                print(pokeType)
                poke.types.add(pokeType)
            poke.save()