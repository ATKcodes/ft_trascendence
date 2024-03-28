from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password= request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/login/thank-you')
        else:
            return render(request, "login/login.html")
    else: 
        return render(request, "login/login.html")

def index2(request, extra_path):
    return render(request, 'login/prova.html')

def thank_you(request):
    return render(request, 'login/thank-you.html')
    
