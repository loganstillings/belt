from django.shortcuts import render, redirect
from .models import User
from ..belt.models import Poke
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    viewsResponse = User.objects.add_user(request.POST)
    if viewsResponse['isRegistered']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('/pokes')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('/')
def success(request):
    if 'user_id' not in request.session:
        messages.error(self, 'Must be logged in!')
        return redirect('/')
    context = {
        'other_users': User.objects.exclude(id = request.session['user_id']),
        'poked_you': Poke.objects.filter(one_getting_poked= request.session['user_id']),
        'count_pokes' : Poke.objects.filter(one_getting_poked= request.session['user_id']).count(),
    }
    return render(request, 'first_app/success.html', context)

def login(request):
    viewsResponse = User.objects.login_user(request.POST)
    if viewsResponse['isLoggedIn']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('/pokes')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
