# -*- coding: utf-8 -*-

import json
import urllib.request
import time
from django.http import HttpResponse

from moviefun.models import *
def insert(request):
	t0=time.clock()	
	t1 = Movie(imdbid = 'tt0000000',
		title = 'insert_test',
		year = '2016',
		rated = '18+',
		released = 'N/A',
		runtime = 'A term',
		genre = 'School',
		director = 'Team 4',
		writer = 'cz8',
		actors = 'Team 4',
		plot = 'An insert action',
		language = 'python',
		awards = '5%',
		poster = 'N/A',
		imdbrating = '5.0',
		imdbvotes = '4',
		type = 'movie')
	t1.save()
	t0=time.clock()-t0
	return HttpResponse("<p>" + str(t0) + "</p>")
