# -*- coding: utf-8 -*-

from django.http import HttpResponse
import time
from moviefun.models import *
def select(request):
        t0=time.clock()
        s=Movie.objects.get(imdbid='tt0000000')
        t0=time.clock()-t0
        response='runningtime: ' + str(t0) + ' ' + s.title
        return HttpResponse("<p>" + response + "</p>")
