# -*- coding: utf-8 -*-

from django.http import HttpResponse

from moviefun.models import *
def select(request):
        s=Movie.objects.filter(year='2007',type='episode')
        response=''
        n=0
        for var in s:
                r=TVPlay.objects.get(imdbid=var.imdbid)
                if r.season=='3':
                        n=n+1
                        response += str(n) + '.' + var.title + ' '
        return HttpResponse("<p>" + response + "</p>")
