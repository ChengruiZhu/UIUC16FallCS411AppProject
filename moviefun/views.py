# -*- coding: utf-8 -*-
from django.http import HttpResponse
from moviefun.models import *
import json

from urllib.request import urlopen

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
    log_max = float(log_1) - 180.0 if float(log_1) > float(log_2) else float(log_2) - 180.0
    log_min = float(log_1) - 180.0 if float(log_1) < float(log_2) else float(log_2) - 180.0
    lat_max = float(lat_1) - 180.0 if float(lat_1) > float(lat_2) else float(lat_2) - 180.0
    lat_min = float(lat_1) - 180.0 if float(lat_1) < float(lat_2) else float(lat_2) - 180.0

    list = Loc.objects.exclude(latitude='N/A')

    log_dist = (log_max - log_min) / log_num
    lat_dist = (lat_max - lat_min) / lat_num

    # l = []
    ss = []
    for i in range(log_num):
        for j in range(lat_num):
            num = 0
            for var in list:
                if var.longitude != "N/A" and log_min + i * log_dist < float(var.longitude) < log_min + (
                    i + 1) * log_dist and lat_min + j * lat_dist < float(
                        var.latitude) < lat_min + (j + 1) * lat_dist:
                    num += 1
                    ss.append(MovieLocR.objects.filter(address_id=var.address)[0])
                    if num >= m_num:
                        break
    movieArr = []
    for var in ss:
        dict = {}
        obj_1 = Movie.objects.get(imdbid=var.imdbid_id)
        obj_2 = Loc.objects.get(address=var.address_id)
        obj_set = RecomR.objects.filter(movie1_id_id=var.imdbid)[:10]
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
        dict['recom0'] = Movie.objects.get(imdbid=obj_set[0].movie2_id_id).title
        dict['recom1'] = Movie.objects.get(imdbid=obj_set[1].movie2_id_id).title
        dict['recom2'] = Movie.objects.get(imdbid=obj_set[2].movie2_id_id).title
        dict['recom3'] = Movie.objects.get(imdbid=obj_set[3].movie2_id_id).title
        dict['recom4'] = Movie.objects.get(imdbid=obj_set[4].movie2_id_id).title
        dict['recom5'] = Movie.objects.get(imdbid=obj_set[5].movie2_id_id).title
        dict['recom6'] = Movie.objects.get(imdbid=obj_set[6].movie2_id_id).title
        dict['recom7'] = Movie.objects.get(imdbid=obj_set[7].movie2_id_id).title
        dict['recom8'] = Movie.objects.get(imdbid=obj_set[8].movie2_id_id).title
        dict['recom9'] = Movie.objects.get(imdbid=obj_set[9].movie2_id_id).title
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

def post_filter(request, lat_1, lat_2, log_1, log_2, year_1, year_2, rate_1, rate_2, isDrama, isAction, isRomance):
    log_max = float(log_1)-180.0 if float(log_1) > float(log_2) else float(log_2)-180.0
    log_min = float(log_1)-180.0 if float(log_1) < float(log_2) else float(log_2)-180.0
    lat_max = float(lat_1)-180.0 if float(lat_1) > float(lat_2) else float(lat_2)-180.0
    lat_min = float(lat_1)-180.0 if float(lat_1) < float(lat_2) else float(lat_2)-180.0

    list = Loc.objects.exclude(latitude='N/A')

    log_dist = (log_max - log_min) / log_num
    lat_dist = (lat_max - lat_min) / lat_num

    ss = []
    for i in range(log_num):
        for j in range(lat_num):
            num=0
            for var in list:
                if var.longitude != "N/A" and log_min+i*log_dist < float(var.longitude) < log_min+(i+1)*log_dist and lat_min+j*lat_dist < float(
                            var.latitude) < lat_min+(j+1)*lat_dist:
                    tmp1 = MovieLocR.objects.filter(address_id = var.address)
                    for subvar in tmp1:
                        tmp2 = Movie.objects.get(imdbid = subvar.imdbid_id)
                        if int(year_1) <= int(tmp2.year[:4]) <= int(year_2) and float(rate_1) <= float(tmp2.imdbrating) <= float(rate_2):
                            if 'drama' in tmp2.genre.lower() and isDrama == "true":
                                num += 1
                                ss.append(MovieLocR.objects.filter(address_id=var.address)[0])
                                if num >= m_num:
                                    break
                                continue
                            if 'action' in tmp2.genre.lower() and isAction == "true":
                                num += 1
                                ss.append(MovieLocR.objects.filter(address_id=var.address)[0])
                                if num >= m_num:
                                    break
                                continue
                            if 'romance' in tmp2.genre.lower() and isRomance == "true":
                                num += 1
                                ss.append(MovieLocR.objects.filter(address_id=var.address)[0])
                                if num >= m_num:
                                    break
                                continue
                            if isDrama == "false" and isAction == "false" and isRomance == "false":
                                num += 1
                                ss.append(MovieLocR.objects.filter(address_id=var.address)[0])
                                if num >= m_num:
                                    break
                                continue
                if num >= m_num:
                    break


    movieArr = []
    for var in ss:
        dict = {}
        obj_1 = Movie.objects.get(imdbid = var.imdbid_id)
        obj_2 = Loc.objects.get(address = var.address_id)
        obj_set = RecomR.objects.filter(movie1_id_id = var.imdbid)[:10]
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
        dict['recom0'] = Movie.objects.get(imdbid=obj_set[0].movie2_id_id).title
        dict['recom1'] = Movie.objects.get(imdbid=obj_set[1].movie2_id_id).title
        dict['recom2'] = Movie.objects.get(imdbid=obj_set[2].movie2_id_id).title
        dict['recom3'] = Movie.objects.get(imdbid=obj_set[3].movie2_id_id).title
        dict['recom4'] = Movie.objects.get(imdbid=obj_set[4].movie2_id_id).title
        dict['recom5'] = Movie.objects.get(imdbid=obj_set[5].movie2_id_id).title
        dict['recom6'] = Movie.objects.get(imdbid=obj_set[6].movie2_id_id).title
        dict['recom7'] = Movie.objects.get(imdbid=obj_set[7].movie2_id_id).title
        dict['recom8'] = Movie.objects.get(imdbid=obj_set[8].movie2_id_id).title
        dict['recom9'] = Movie.objects.get(imdbid=obj_set[9].movie2_id_id).title
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
    addr = addr.strip().replace("_", "+")
    req = urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '&key=' + API_KEY)
    the_page = req.read()

    parsed_json = json.loads(the_page.decode('utf-8'))

    if parsed_json['status'] == 'OK':
        nelat = parsed_json['results'][0]['geometry']['bounds']['northeast']['lat']
        nelng = parsed_json['results'][0]['geometry']['bounds']['northeast']['lng']
        swlat = parsed_json['results'][0]['geometry']['bounds']['southwest']['lat']
        swlng = parsed_json['results'][0]['geometry']['bounds']['southwest']['lng']


        log_min = float(swlng)
        log_max = float(nelng)
        lat_min = float(swlat)
        lat_max = float(nelat)

        list = Loc.objects.exclude(latitude='N/A')

        log_dist = (log_max - log_min) / log_num
        lat_dist = (lat_max - lat_min) / lat_num

        # l = []
        ss = []
        for i in range(log_num):
            for j in range(lat_num):
                num = 0
                for var in list:
                    if var.longitude != "N/A" and log_min + i * log_dist < float(var.longitude) < log_min + (
                                i + 1) * log_dist and lat_min + j * lat_dist < float(
                        var.latitude) < lat_min + (j + 1) * lat_dist:
                        num += 1
                        ss.append(MovieLocR.objects.filter(address_id=var.address)[0])
                        if num >= m_num:
                            break
        movieArr = []
        for var in ss:
            dict = {}
            obj_1 = Movie.objects.get(imdbid=var.imdbid_id)
            obj_2 = Loc.objects.get(address=var.address_id)
            obj_set = RecomR.objects.filter(movie1_id_id=var.imdbid)[:10]
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
            dict['recom0'] = Movie.objects.get(imdbid=obj_set[0].movie2_id_id).title
            dict['recom1'] = Movie.objects.get(imdbid=obj_set[1].movie2_id_id).title
            dict['recom2'] = Movie.objects.get(imdbid=obj_set[2].movie2_id_id).title
            dict['recom3'] = Movie.objects.get(imdbid=obj_set[3].movie2_id_id).title
            dict['recom4'] = Movie.objects.get(imdbid=obj_set[4].movie2_id_id).title
            dict['recom5'] = Movie.objects.get(imdbid=obj_set[5].movie2_id_id).title
            dict['recom6'] = Movie.objects.get(imdbid=obj_set[6].movie2_id_id).title
            dict['recom7'] = Movie.objects.get(imdbid=obj_set[7].movie2_id_id).title
            dict['recom8'] = Movie.objects.get(imdbid=obj_set[8].movie2_id_id).title
            dict['recom9'] = Movie.objects.get(imdbid=obj_set[9].movie2_id_id).title
            dict['error'] = '0'
            dict['nelat'] = nelat
            dict['nelng'] = nelng
            dict['swlat'] = swlat
            dict['swlng'] = swlng
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
        movieArr = []
        dict = {}
        dict['error'] = '1'
        movieArr.append(dict)
        if request.method == 'GET':
            response = HttpResponse(json.dumps(movieArr))
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            response["Content-Type"] = "application/json; charset=uft-8"
            return response



