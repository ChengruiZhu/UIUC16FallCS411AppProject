# -*- coding: utf-8 -*-

from django.http import HttpResponse
from moviefun.models import *


def insert_loc(request):

    inputFile = open("/home/cz8/moviesite/data/address")

    line = inputFile.readline()

    i=0
    cnt=0

    while len(line) != 0:
        imdbNum = line.split('|')[0]
        addr = line.split('|')[1]
        s = Movie.objects.get(imdbid=imdbNum)
        t4 = Loc(address = addr)
        t4.save()

        t5 = MovieLocR(imdbid = s,
                 address = t4)
        t5.save()

        i=i+1

        if i>1:
            break

    return HttpResponse("<p>地址添加成功！</p>")
