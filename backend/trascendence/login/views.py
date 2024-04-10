from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from . import models
from . import serializers
from django.shortcuts import get_object_or_404
# Create your views here.

class UserViewSet(APIView):
    def get (self, request):
        if id:
            item = models.User.objects.get(id=id)
            serializer = serializers.UserSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        users = models.User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        item = models.User.objects.get(id=id)
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        item = models.User.objects.get(id=id)
        serializer = serializers.UserSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, id=None):
        item = models.User.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "User deleted successfully"}, status=status.HTTP_200_OK)



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
    
