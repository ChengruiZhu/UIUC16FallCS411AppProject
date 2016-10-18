# -*- coding: utf-8 -*-

from django.http import HttpResponse
from moviefun.models import *

def insert(request):
	dic={'movie_name':[], 
	'year':[], 
	'cast':[],
	'rating':[],
	'genre':[],
	'director':[],
	'city':[],
	'country':[],
	'title':[],
	'time':[],
	'season_number':[],
	'episode_number':[]}

