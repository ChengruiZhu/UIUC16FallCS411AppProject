# -*- coding: utf-8 -*-

from django.http import HttpResponse

from moviefun.models import *

# 数据库操作
def testdb(request):
	#test = Movie(name='Captain America',year=2016,cast='Steve Rogers',rating=0.0,genre='popcorn',cover='?',director='not known')
	#test.save()
	#test2 = Movie(name='Avengers2',year=2015,cast='Tony Stark',rating=0.0,genre='popcorn',cover='?',director='not known')
	#test2.save()	
	t1 = Movie(name='Superman vs Batman',year=2016,cast='Superman',rating=0.0,genre='popcorn',cover='?',director='not known')
	t1.save()
	t2 = Movie(name='Superman',year=2015,cast='Superman',rating=0.0,genre='popcorn',cover='?',director='not known')
	t2.save()
	t3 = Movie(name='Forrest Gump',year=1994,cast='Gump',rating=4.9,genre='story',cover='?',director='not known')
	t3.save()
	t4 = Movie(name='Pulp Fiction',year=1994,cast='Many',rating=4.9,genre='comedy',cover='?',director='not known')
	t4.save()
	response = Movie.objects.get(id=1)
	return HttpResponse("<p>" + response.name + "</p>")

