from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        print(request.POST["username"])
        return HttpResponseRedirect('/login/thank-you')
    else: 
        return render(request, "login/login.html")

def index2(request, extra_path):
    return render(request, 'login/prova.html')

def thank_you(request):
    if request.method == 'POST':
        print(request.POST["username"])
        print(request.POST["password"]) 
    return render(request, 'login/thank-you.html')
    
