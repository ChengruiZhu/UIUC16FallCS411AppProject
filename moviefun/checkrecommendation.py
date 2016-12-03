# -*- coding: utf-8 -*-

import json
import urllib.request

from django.http import HttpResponse

from moviefun.models import *

def checkrecommendation(request):
    list = Movie.objects.all()
    for var in list:
        reclist = RecomR.objects.filter(movie1_id_id = var.imdbid)
        if len(reclist) < 10:
            return HttpResponse("<p>" + var.imdbid +"</p>")
    return HttpResponse("<p>数据添加成功！</p>")