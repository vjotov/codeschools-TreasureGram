from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure, Location
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import TreasureForm, LoginForm


# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    context = {'treasures': treasures, 'form':form}
    return render(request, 'index.html', context)


def home(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'home.html', context)


def datail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    context = {'treasure': treasure}
    return render(request, "detail.html", context)

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save(commit = False)
        treasure.user = request.user
        treasure.save()

    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    context = {'username': username, 'treasures': treasures}
    return render(request, 'profile.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled!")
            else:
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})