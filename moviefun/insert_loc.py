# -*- coding: utf-8 -*-

from django.http import HttpResponse
from moviefun.models import *


def insert_loc(request):

    inputFile = open("/home/cz8/moviesite/data/addr")

    line = inputFile.readline()

    i=0
    cnt=0

    while len(line) != 0:
        imdbNum = line.split('|')[0]
        addr = line.split('|')[1]
        s = Movie.objects.get(imdbid="tt"+imdbNum)
        t4 = Loc(address = addr)
        t4.save()

        t5 = MovieLocR(imdbid = s,
                 address = t4)
        t5.save()
        
        line = inputFile.readline()
        #i=i+1

    return HttpResponse("<p>地址添加成功！</p>")
