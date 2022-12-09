from django.shortcuts import render
from .forms import *

def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
