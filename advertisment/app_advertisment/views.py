from django.shortcuts import render
from django.http import HttpResponse


def index(reqests):
    return render(reqests, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')