from django.http import HttpResponse
from django.shortcuts import render_to_response

from main.models import Contact

def home(request):

    return render_to_response('index.html')

def tomato(request):
    contacts = Contact.objects.all()
    pizza_taste = "yum"
    return render_to_response('tomato.html',
                              locals())
