from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):  
    return render(request, 'index.html', {'treasures': treasures})

def home(request):
    location_name = "Fool's Falls"
    predators = 'Scorpions, Snakes'
    context = {'location_name': location_name,
               'predators': predators}
    return render(request, 'home.html', context)
    

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",'/static/images/nugget.png'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO",'/static/images/fools-gold.png'),
    Treasure('Coffee Can', 20.00, 'tin', 'Aacme, CA','/static/images/coffee-can.png'),
]
