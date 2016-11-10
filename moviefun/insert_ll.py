# -*- coding: utf-8 -*-

from django.http import HttpResponse
from moviefun.models import *


def insert_ll(request):
    inputFile = open("/home/cz8/moviesite/data/geo")

    line = inputFile.readline()

    while len(line) != 0:
        imdbNum = line.split('|')[0]
        geo = line.split('|')[1]
        x = geo.split(',')[0]
        y = geo.split(',')[1]

        s1 = MovieLocR.objects.get(imdbid = "tt" + imdbNum)
        s2 = Loc.objects.get(address = s1)
        s2.latitude = x
        s2.longitude = y
        s2.save()

        line = inputFile.readline()
        # i=i+1

    return HttpResponse("<p>坐标添加成功！</p>")
