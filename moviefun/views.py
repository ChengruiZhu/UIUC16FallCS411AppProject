# -*- coding: utf-8 -*-
#from django.http import HttpResponse

STATIC_URL = '/static/'

from django.shortcuts import render
def index(request):
    context={}
    context['hello']='Welcome to the moviefun!'
    #return HttpResponse("Hello, world. You're at the moviefun index.")
    return render(request,'index.html', context)
# Create your views here.
