# -*- coding: utf-8 -*-

import json
import urllib.request

from django.http import HttpResponse

from moviefun.models import *

# from get_loc import getLocation



def insert_recommendation(request):
    list = Movie.objects.all()
    for var in list:
        year = var.year;
        if '–' in year:
            year = year[:-1]
        tmplist1 = Movie.objects.filter(genre__icontains=var.genre).exclude(imdbid=var.imdbid)
        tmplist = tmplist1
        if len(tmplist) < 10:
            tmplist2 = Movie.objects.filter(director__icontains=var.director).exclude(imdbid=var.imdbid)
            tmplist = tmplist | tmplist2
            tmplist.distinct()
            numOfMovies = len(tmplist)
            while (numOfMovies < 10):
                tmplist3 = Movie.objects.filter(year__icontains=year).exclude(imdbid=var.imdbid)
                tmplist = tmplist | tmplist3
                tmplist.distinct()
                numOfMovies = len(tmplist)
                year = year[:-1]
        else:
            tmplist = tmplist.filter(director__icontains=var.director)
            numOfMovies = len(tmplist)
            while (numOfMovies < 10):
                tmplist3 = tmplist1.filter(year__icontains=year)
                tmplist = tmplist | tmplist3
                tmplist.distinct()
                numOfMovies = len(tmplist)
                year = year[:-1]
        for tmpvar in tmplist[:10]:
            t = RecomR(movie1_id=var,
                       movie2_id=tmpvar)
            t.save()

    return HttpResponse("<p>数据添加成功！</p>")



