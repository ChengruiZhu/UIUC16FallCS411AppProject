# -*- coding: utf-8 -*-

import json
import urllib2

from django.http import HttpResponse

from moviefun.models import *

def insert(request):

        for i in range(3603346, 3603456):

                req = urllib2.Request('http://www.omdbapi.com/?i=tt' + str(i)+'&plot=short&r=json')
                response = urllib2.urlopen(req)
                the_page = response.read()

                parsed_json = json.loads(the_page)
                # print(parsed_json)
                if parsed_json['Response'] == 'True':
                        t1 = Movie(title = parsed_json['Title'],
                                year = parsed_json['Year'],
                                rated = parsed_json['Rated'],
                                released = parsed_json['Released'],
                                runtime = parsed_json['Runtime'],
                                genre = parsed_json['Genre'],
                                director = parsed_json['Director'],
                                writer = parsed_json['Writer'],
                                actors = parsed_json['Actors'],
                                plot = parsed_json['Plot'],
                                language = parsed_json['Language'],
                                awards = parsed_json['Awards'],
                                poster = parsed_json['Poster'],
                                metascore = parsed_json['Metascore'],
                                imdbrating = parsed_json['imdbRating'],
                                imdbvotes = parsed_json['imdbVotes'],
                                imdbid = parsed_json['imdbID'],
                                type = parsed_json['Type'])
                        t1.save()

                        if parsed_json['Type'] == 'episode':
                                t2 = TVPlay(movie_id = t1,
                                        season = parsed_json['Season'],
                                        episode = parsed_json['Episode'],
                                        seriesid = parsed_json['seriesID'])

                                t2.save()

                        if parsed_json['Type'] == 'series':
                                t3 = TVSeries(movie_id = t1,
                                        totalseasons = parsed_json['totalSeasons'])
                                t3.save()

                             # print(parsed_json)
        return HttpResponse("<p>数据添加成功！</p>")