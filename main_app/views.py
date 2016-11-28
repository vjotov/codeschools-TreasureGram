from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure, Location
from .forms import TreasureForm


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
    form = TreasureForm(request.POST)
    if form.is_valid():
        form.save(commit = True)

    return HttpResponseRedirect('/')
