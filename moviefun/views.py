# -*- coding: utf-8 -*-
from django.http import HttpResponse
from moviefun.models import *
import json

import urllib.request

API_KEY = 'AIzaSyAiAnz_K18bDdmJoCNCVFMjV0QqxfvuVb8'

STATIC_URL = '/static/'

radius = 10

m_num = 1
log_num = 10
lat_num = 10


from django.shortcuts import render
def index(request):
    context={}
    context['hello']='Welcome to the moviefun!'
    #return HttpResponse("Hello, world. You're at the moviefun index.")
    return render(request,'index.html', context)
# Create your views here.

def love(request, imdbid):
    s = Like.objects.filter(imdbid = imdbid)
    if len(s) == 0:
        t = Like(imdbid = imdbid, like = 1)
        t.save()
    else:
        t = Like.objects.get(imdbid = imdbid)
        t.like = t.like + 1
        t.save()
    if request.method ==  'GET':
        response = HttpResponse('insert success!')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

def queryfirst(qs):
    r = list(qs[:1])
    if r:
        return r[0]
    return None
  

def findMovie(list, long_min, long_max, la_min, la_max):
    for var in list:
        if var.longitude != "N/A":
            if float(var.longitude) > long_min and float(var.longitude) < long_max \
                    and float(var.latitude) > la_min and float(var.latitude) < la_max:
                s = MovieLocR.objects.filter(address = var.address)
                return queryfirst(s)

def post_detail(request, lat_1, lat_2, log_1, log_2):
    log_max = float(log_1)-180.0 if float(log_1) > float(log_2) else float(log_2)-180.0
    log_min = float(log_1)-180.0 if float(log_1) < float(log_2) else float(log_2)-180.0
    lat_max = float(lat_1)-180.0 if float(lat_1) > float(lat_2) else float(lat_2)-180.0
    lat_min = float(lat_1)-180.0 if float(lat_1) < float(lat_2) else float(lat_2)-180.0

    list = Loc.objects.exclude(latitude = 'N/A')

    l = []
    ss = []
    for var in list:
        if var.longitude != "N/A":
            if float(var.longitude) > log_min and float(var.longitude) < log_max \
                    and float(var.latitude) > lat_min and float(var.latitude) < lat_max:
                l.append(var)

    log_dist = (log_max-log_min)/log_num
    lat_dist = (lat_max-lat_min)/lat_num
    for i in range(log_num):
        for j in range(lat_num):
            tmp = findMovie(l, log_min+i*log_dist,
                                  log_min+(i+1)*log_dist,
                                  lat_min+j*lat_dist,
                                  lat_min+(j+1)*lat_dist)
            if tmp != None:
                ss.append(tmp)
    movieArr = []
    for var in ss:
        dict = {}
        obj_1 = Movie.objects.get(imdbid = var.imdbid_id)
        obj_2 = Loc.objects.get(address  = var.address_id)
        # obj_3 = RecomR.objects.filter(movie1_id_id = var.imdb_id)[:10]
        # rec = ""
        # for recvar in obj_3:
        #     if rec == "":
        #         rec += recvar.movie2_id_id
        #     else :
        #         rec = rec + ";" +recvar.movie2_id_id
        obj = Like.objects.filter(imdbid = var.imdbid_id)
        if len(obj) == 0:
            dict['like'] = 0
        else:
            obj_3 = Like.objects.get(imdbid = var.imdbid_id)
            dict['like'] = obj_3.like
        dict['imdbid'] = obj_1.imdbid
        dict['title'] = obj_1.title
        dict['year'] = obj_1.year
        dict['rated'] = obj_1.rated
        dict['released'] = obj_1.released
        dict['runtime'] = obj_1.runtime
        dict['genre'] = obj_1.genre
        dict['director'] = obj_1.director
        dict['writer'] = obj_1.writer
        dict['actors'] = obj_1.actors
        dict['plot'] = obj_1.plot
        dict['language'] = obj_1.language
        dict['awards'] = obj_1.awards
        dict['poster'] = obj_1.poster
        dict['idbrating'] = obj_1.imdbrating
        dict['imdbvotes'] = obj_1.imdbvotes
        dict['type'] = obj_1.type
        dict['address'] = obj_2.address.strip()
        dict['latitude'] = obj_2.latitude
        dict['longitude'] = obj_2.longitude.strip()
        # dict['recommendation'] = rec
        movieArr.append(dict)

    # loaded_r = json.loads(r)
    #loaded_r['rating'] #Output 3.5
    if request.method ==  'GET':
        response = HttpResponse(json.dumps(movieArr))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        response["Content-Type"] = "application/json; charset=uft-8"
        return response
    # elif request.method ==  'POST':
    #     return HttpResponse("<p>" + str + "</p>")

def post_filter(request, lat_1, lat_2, log_1, log_2, year_1, year_2, rate_1, rate_2, isDrama, isAction, isRomance):
    log_max = float(log_1)-180.0 if float(log_1) > float(log_2) else float(log_2)-180.0
    log_min = float(log_1)-180.0 if float(log_1) < float(log_2) else float(log_2)-180.0
    lat_max = float(lat_1)-180.0 if float(lat_1) > float(lat_2) else float(lat_2)-180.0
    lat_min = float(lat_1)-180.0 if float(lat_1) < float(lat_2) else float(lat_2)-180.0

    # list_all = MovieLocR.objects.all().select_related('imdbid').select_related('address')
    # list_genre = MovieLocR.objects.none().select_related('imdbid').select_related('address')
    #
    # if isDrama == 'true':
    #     list_genre = list_genre | list_all.filter(imdbid__genre__icontains = 'drama')
    # if isAction == 'true':
    #     list_genre = list_genre | list_all.filter(imdbid__genre__icontains = 'action')
    # if isRomance == 'true':
    #     list_genre = list_genre | list_all.filter(imdbid__genre__icontains = 'Romance')
    # list_genre.distinct()
    #
    # list_year = list_genre.filter(imdbid__year__icontains = year_1)
    #
    # for i in range(int(year_1)+1, int(year_2)+1):
    #     i_str = str(i)
    #     list_year = list_year | list_genre.filter(imdbid__year__icontains = i_str)
    #
    # list_rate = list_year.filter(imdbid__imdbrating = rate_1)
    #
    # i_float = float(rate_1)
    # while(i_float <= float(rate_2)):
    #     i_float += 0.1
    #     i_str = str(i_float)
    #     list_rate = list_rate | list_year.filter(imdbid__imdbrating = i_str)
    #
    # list = list_rate

    # list = MovieLocR.objects.all().select_related('imdbid').select_related('address')
    list = Loc.objects.exclude(latitude='N/A')

    log_dist = (log_max - log_min) / log_num
    lat_dist = (lat_max - lat_min) / lat_num

    # l = []
    ss = []
    for i in range(log_num):
        for j in range(lat_num):
            num=0
            for var in list:
                if var.longitude != "N/A" and log_min+i*log_dist < float(var.longitude) < log_min+(i+1)*log_dist and lat_min+j*lat_dist < float(
                            var.latitude) < lat_min+(j+1)*lat_dist:
                    num += 1
                    ss.append(MovieLocR.objects.filter(address_id = var.address)[0])
                    if num >= m_num:
                        break
    movieArr = []
    for var in ss:
        dict = {}
        obj_1 = Movie.objects.get(imdbid = var.imdbid_id)
        obj_2 = Loc.objects.get(address = var.address_id)
        # obj_3 = RecomR.objects.filter(movie1_id_id = var.imdb_id)[:10]
        # rec = ""
        # for recvar in obj_3:
        #     if rec == "":
        #         rec += recvar.movie2_id_id
        #     else :
        #         rec = rec + ";" +recvar.movie2_id_id
        obj = Like.objects.filter(imdbid = var.imdbid_id)
        if len(obj) == 0:
            dict['like'] = 0
        else:
            obj_3 = Like.objects.get(imdbid = var.imdbid_id)
            dict['like'] = obj_3.like
        dict['imdbid'] = obj_1.imdbid
        dict['title'] = obj_1.title
        dict['year'] = obj_1.year
        dict['rated'] = obj_1.rated
        dict['released'] = obj_1.released
        dict['runtime'] = obj_1.runtime
        dict['genre'] = obj_1.genre
        dict['director'] = obj_1.director
        dict['writer'] = obj_1.writer
        dict['actors'] = obj_1.actors
        dict['plot'] = obj_1.plot
        dict['language'] = obj_1.language
        dict['awards'] = obj_1.awards
        dict['poster'] = obj_1.poster
        dict['idbrating'] = obj_1.imdbrating
        dict['imdbvotes'] = obj_1.imdbvotes
        dict['type'] = obj_1.type
        dict['address'] = obj_2.address.strip()
        dict['latitude'] = obj_2.latitude
        dict['longitude'] = obj_2.longitude.strip()
        # dict['recommendation'] = rec
        movieArr.append(dict)

    # loaded_r = json.loads(r)
    #loaded_r['rating'] #Output 3.5
    if request.method ==  'GET':
        response = HttpResponse(json.dumps(movieArr))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        response["Content-Type"] = "application/json; charset=uft-8"
        return response

def findMoviesByLoc(request, addr):
    addr = addr.strip().replace(" ", "+")
    req = urllib.Request('https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '&key=' + API_KEY)
    response = urllib.urlopen(req)
    the_page = response.read()

    parsed_json = json.loads(the_page)

    if parsed_json['status'] == 'OK':
        lat = parsed_json['results'][0]['geometry']['location']['lat']
        lng = parsed_json['results'][0]['geometry']['location']['lng']

        log_min = float(lng) - radius
        log_max = float(lng) + radius
        lat_min = float(lat) - radius
        lat_max = float(lat) + radius
        list = Loc.objects.all()

        l = []
        ss = []
        for var in list:
            if var.longitude != "N/A":
                if float(var.longitude) > log_min and float(var.longitude) < log_max \
                        and float(var.latitude) > lat_min and float(var.latitude) < lat_max:
                    l.append(var)

        log_dist = (log_max - log_min) / log_num
        lat_dist = (lat_max - lat_min) / lat_num
        for i in range(log_num):
            for j in range(lat_num):
                tmp = findMovie(l, log_min + i * log_dist,
                                log_min + (i + 1) * log_dist,
                                lat_min + j * lat_dist,
                                lat_min + (j + 1) * lat_dist)
                if tmp != None:
                    ss.append(tmp)
        movieArr = []
        for var in ss:
            dict = {}
            obj_1 = Movie.objects.get(imdbid=var.imdbid_id)
            obj_2 = Loc.objects.get(address=var.address_id)
            # obj_3 = RecomR.objects.filter(movie1_id_id = var.imdb_id)[:10]
            # rec = ""
            # for recvar in obj_3:
            #     if rec == "":
            #         rec += recvar.movie2_id_id
            #     else :
            #         rec = rec + ";" +recvar.movie2_id_id
            obj = Like.objects.filter(imdbid=var.imdbid_id)
            if len(obj) == 0:
                dict['like'] = 0
            else:
                obj_3 = Like.objects.get(imdbid=var.imdbid_id)
                dict['like'] = obj_3.like
            dict['imdbid'] = obj_1.imdbid
            dict['title'] = obj_1.title
            dict['year'] = obj_1.year
            dict['rated'] = obj_1.rated
            dict['released'] = obj_1.released
            dict['runtime'] = obj_1.runtime
            dict['genre'] = obj_1.genre
            dict['director'] = obj_1.director
            dict['writer'] = obj_1.writer
            dict['actors'] = obj_1.actors
            dict['plot'] = obj_1.plot
            dict['language'] = obj_1.language
            dict['awards'] = obj_1.awards
            dict['poster'] = obj_1.poster
            dict['idbrating'] = obj_1.imdbrating
            dict['imdbvotes'] = obj_1.imdbvotes
            dict['type'] = obj_1.type
            dict['address'] = obj_2.address.strip()
            dict['latitude'] = obj_2.latitude
            dict['longitude'] = obj_2.longitude.strip()
            # dict['recommendation'] = rec
            movieArr.append(dict)

        # loaded_r = json.loads(r)
        # loaded_r['rating'] #Output 3.5
        if request.method == 'GET':
            response = HttpResponse(json.dumps(movieArr))
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            response["Content-Type"] = "application/json; charset=uft-8"
            return response

    else:
        if request.method == 'GET':
            response = HttpResponse("No this place!")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            response["Content-Type"] = "application/json; charset=uft-8"
            return response



