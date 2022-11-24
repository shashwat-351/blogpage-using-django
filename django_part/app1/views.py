from django.shortcuts import render
from .models import blognews
# Create your views here.

def client(request):
    bnews = blognews.objects.all()
    data = {
        'bnews': bnews
    }
    return render(request,'client.html',data)