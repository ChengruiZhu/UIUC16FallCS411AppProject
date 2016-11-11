# -*- coding: utf-8 -*-
from django.http import HttpResponse
from moviefun.models import *

STATIC_URL = '/static/'

m_num = 3
log_num = 10
lat_num = 10


from django.shortcuts import render
def index(request):
    context={}
    context['hello']='Welcome to the moviefun!'
    #return HttpResponse("Hello, world. You're at the moviefun index.")
    return render(request,'index.html', context)
# Create your views here.

def findMovie(list, long_min, long_max, la_min, la_max):
    l = MovieLocR.objects.none()
    for var in list:
        if len(l) < m_num:
            if var.longitude != "N/A":
                if float(var.longitude) > long_min and float(var.longitude) < long_max \
                        and float(var.latitude) > la_min and float(var.latitude) < la_max:
                    s = MovieLocR.objects.filter(address = var.address)[:1]
                    l = l | s
                    l.distinct()
        else:
            break
    return list(l)


# def post_detail(request, lat_1, lat_2, log_1, log_2):
#     log_max = log_1 if log_1 > log_2 else log_2
#     log_min = log_1 if log_1 < log_2 else log_2
#     lat_max = lat_1 if lat_1 > lat_2 else lat_2
#     lat_min = lat_1 if lat_1 < lat_2 else lat_2
#
#     list = Loc.objects.all()
#
#     l = []
#     set = []
#     for var in list:
#         if var.longitude != "N/A":
#             if float(var.longitude) > log_min and float(var.longitude) < log_max \
#                     and float(var.latitude) > lat_min and float(var.latitude) < lat_max:
#                 l.append(var)
#
#     log_dist = (log_max-log_min)/log_num
#     lat_dist = (lat_max-lat_min)/lat_num
#     for i in range(log_num):
#         for j in range(lat_num):
#             set = set + findMovie(l, log_min+i*log_dist,
#                                   log_min+(i+1)*log_dist,
#                                   lat_min+j*lat_dist,
#                                   lat_min+(j+1)*lat_dist)
#     str = ''
#     for var in set:
#         str = str + var.imdbid + ' '
#     return HttpResponse("<p>" + str + "</p>")

def post_detail(request, id):
    return HttpResponse("<p>" + str(id) + "</p>")



