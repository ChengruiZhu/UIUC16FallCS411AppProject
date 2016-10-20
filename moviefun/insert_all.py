# -*- coding: utf-8 -*-

import json
import urllib.request

from django.http import HttpResponse

from moviefun.models import *

start = 1000000 
end = 1000500

def insert(request):

        for i in range(start, end):

                req = urllib.request.Request('http://www.omdbapi.com/?i=tt' + str(i)+'&plot=short&r=json')
                response = urllib.request.urlopen(req)
                the_page = response.readall().decode('utf-8')
                parsed_json = json.loads(the_page)
                #print(parsed_json)
                if parsed_json['Response'] == 'True' and parsed_json['Poster'] != 'N/A' and parsed_json['imdbRating'] != 'N/A' and parsed_json['Country'] != 'N/A':
                        t1 = Movie(imdbid = parsed_json['imdbID'],
                                title = parsed_json['Title'],
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
                                #metascore = parsed_json['Metascore'],
                                imdbrating = parsed_json['imdbRating'],
                                imdbvotes = parsed_json['imdbVotes'],
                                type = parsed_json['Type'])
                        t1.save()

                        if parsed_json['Type'] == 'episode' and parsed_json['Episode'] != 'N/A' and parsed_json['Season'] != 'N/A' and parsed_json['seriesID'] != 'N/A':
                                t2 = TVPlay(imdbid = t1,
                                        season = parsed_json['Season'],
                                        episode = parsed_json['Episode'],
                                        seriesid = parsed_json['seriesID'])

                                t2.save()

                        if parsed_json['Type'] == 'series':
                                t3 = TVSeries(seriesid = t1,
                                        totalseasons = parsed_json['totalSeasons'])
                                t3.save()

                             # print(parsed_json)
        return HttpResponse("<p>数据添加成功！</p>")
