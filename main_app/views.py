from django.shortcuts import render
from .models import Treasure, Location


# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})


def home(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'home.html', context)


def datail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    context = {'treasure': treasure}
    return render(request, "detail.html", context)
