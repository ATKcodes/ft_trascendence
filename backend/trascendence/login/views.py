from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = render_to_string('login/login.html')
    return HttpResponse(response)