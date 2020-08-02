from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def get_contacts(request):
    return HttpResponse('First contact to views')
