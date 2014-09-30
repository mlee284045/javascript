from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pokemon.models import Pokemon


def all_pokemon(request):
    pokemon = Pokemon.objects.all()
    data = serializers.serialize('json', pokemon)
    return HttpResponse(data, content_type='application/json')