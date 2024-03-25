from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    try:
        return render(request, 'login/login.html')
    except:  
        return render(request, 'login/prova.html')

def index2(request, extra_path):
    return render(request, 'login/prova.html')
    
