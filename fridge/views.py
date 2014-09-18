# Create your views here.
import datetime
from functools import partial
import json
import logging
import os.path

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django import forms
from django.contrib import messages
from django.utils.timezone import now as utcnow

from . import models
from .models import Location, Item, Product, Shelf


def inventory(request):

    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            product = Product.objects.get(name=itemform.cleaned_data['name'])
            etime = utcnow() + datetime.timedelta(days=product.lifetime)
            item = Item(product=product, etime=etime, loc=product.loc,
                        shelf=Shelf.objects.get(name='Shelf 1'))
            item.save()
#            return HttpResponseRedirect('/thanks/')
    else:
        itemform = ItemForm()

    items = Item.objects.all()


    return render(request, 'fridge/inventory.html', locals())

class ItemForm(forms.Form):
        name = forms.CharField(label='New item', max_length=64)

def complete_item(request):
    print request.REQUEST
    search_qs = Product.objects.filter(name__istartswith=request.REQUEST['search'])
    print search_qs.all()
    results = []
    for r in search_qs:
        results.append(r.name)
    resp = request.REQUEST['callback'] + '(' + json.dumps(results) + ');'
    print resp
    return HttpResponse(resp, content_type='application/json')
