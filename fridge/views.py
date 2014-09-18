# Create your views here.

from functools import partial
import json
import logging
import os.path

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django import forms
from django.contrib import messages

from . import models
from .models import Location, Item, Product, Shelf


def inventory(request):
    items = Item.objects.all()
    return render(request, 'fridge/inventory.html', locals())

