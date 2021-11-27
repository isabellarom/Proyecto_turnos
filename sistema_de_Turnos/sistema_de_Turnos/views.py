from django.http import HttpResponse
from django.shortcuts import render

def mostrarlogin(request):
    return render(request,"login.html")