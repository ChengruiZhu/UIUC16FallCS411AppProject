# -*- coding: utf-8 -*-
#from django.http import HttpResponse

from django.shortcuts import render
def index(request):
    context={}
    context['hello']='Welcome to the moviefun!'
    #return HttpResponse("Hello, world. You're at the moviefun index.")
    return render(request,'homepage.html', context)
# Create your views here.
