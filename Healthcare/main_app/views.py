from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicecard

# Create your views here.
def index(request):
    scard = Servicecard.objects.all()
    return render(request,'index.html', { 'scards': scard })

def bookbed(request):
    return render(request,'bookbed.html')
