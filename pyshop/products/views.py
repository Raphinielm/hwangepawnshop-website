from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# /products -> index


def new(request):
    return HttpResponse("""W
                             E
                               L
                                 C 
                                   O
                                     M
                                       E 
                                        
                                         TO
                                         
                                         H W A N G E 
                                         
                                         P 
                                           A
                                             W
                                               N 
                                                 SHOP""")


def index(request):
    products = Product.objects.all
    return render(request, 'index.html', {'products': products})
# Create your views here.



def available(request):
    return HttpResponse('Available products at the moment')

