from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):  
    return render(request, 'index.html', {'treasures': treasures})

def home(request):
    return HttpResponse('Welcome Home Travelers!')
    

class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
    Treasure('Coffee Can', 20.00, 'tin', 'Aacme, CA'),
]
