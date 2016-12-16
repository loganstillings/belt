from django.shortcuts import render, redirect
from ..first_app.models import User
from .models import Poke
# Create your views here.
def add_poke(request, user_id):
    poker = User.objects.get(id = request.session['user_id'])
    pokee = User.objects.get(id = user_id)
    new_poke = Poke.objects.create(one_poking= poker, one_getting_poked=pokee)
    times_people_poked_you = Poke.objects.filter(one_poking = user_id, one_getting_poked=poker).count()
    request.session['history'] = Poke.objects.filter(one_getting_poked=pokee).count()

    return redirect('/pokes')
