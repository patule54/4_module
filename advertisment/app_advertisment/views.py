from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

def index(reqests):
    advertisements= Advertisement.objects.all()
    context = {'advertisements':advertisements}
    return render(reqests, 'index.html',context)

def top_sellers(request):
    return render(request, 'top-sellers.html')