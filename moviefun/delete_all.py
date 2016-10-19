# -*- coding: utf-8 -*-

from django.http import HttpResponse

from moviefun.models import *

def delete_all(request):
	Movie.objects.all().delete()
	Loc.objects.all().delete()
	MovieLocR.objects.all().delete()
	RecomR.objects.all().delete()
	TVPlay.objects.all().delete()
	TVSeries.objects.all().delete()
	return HttpResponse("<p>删除成功</p>")
