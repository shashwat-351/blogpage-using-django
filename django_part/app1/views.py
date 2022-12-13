from django.shortcuts import render
from .models import blognews
# Create your views here.


def client(request):
    bnews = blognews.objects.all()
    data = {
        'bnews': bnews
    }
    return render(request, 'base.html', data)

def contact_us(request):
    return render(request, 'contact_us.html')
#def client(request):
 #   return render(request,'base.html')