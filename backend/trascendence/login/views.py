from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login ,logout
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def thank_you(request):
    return render(request,'login/thank-you.html')


def index2(request, extra_path):
    return render(request, 'login/prova.html')

def index(request):

    if request.method == "POST":
        print("sono in index")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("sono qui")
            return(redirect('thank-you'))
        else:
            print("ciao2")
            return(redirect('login'))
    else:
        print("ciaooo")
        return(render(request, 'login/login.html'))


