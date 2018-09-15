from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Product
import math

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'amadon/index.html', context)

def process(request):
    # if not in session:
    #     request.session['currenttotal']=0
    #     request.session['totalitems']=0
    #     request.session['totalprice']=0
    count = Product.objects.all().count()
    totalprice = 0
    totalitems = 0
    for i in range (1, count+1):
        currenttotal = 0.0
        tempitem=Product.objects.get(id=i)
        currenttotal += float(request.POST[str(i)+'quantity']) * tempitem.price
        totalprice += currenttotal
        totalitems += int(request.POST[str(i)+'quantity'])
    request.session['currenttotal']=currenttotal
    request.session['totalitems']+=totalitems
    request.session['totalprice']+=totalprice
    return redirect('/amadon/thank_you')


def result(request):
    return render(request, 'amadon/confirm.html')