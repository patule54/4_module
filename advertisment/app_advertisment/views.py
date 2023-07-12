from django.shortcuts import render
from django.http import HttpResponse


def index(reqests):
    return HttpResponse('это мой первый сайт!!!')
