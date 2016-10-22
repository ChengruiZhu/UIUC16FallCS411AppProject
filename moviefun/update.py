# -*- coding: utf-8 -*-

from django.http import HttpResponse
import time
from moviefun.models import *

# 数据库操作
def update(request):
	# 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
	t0=time.clock()
	test1 = Movie.objects.get(imdbid='tt0000001')
	test1.title = 'UIUC16FallCS411AppProject'
	test1.save()
	
	# 另外一种方式
	#Test.objects.filter(id=1).update(name='w3cschool菜鸟教程')
	
	# 修改所有的列
	# Test.objects.all().update(name='w3cschool菜鸟教程')
	t0=time.clock()-t0
	return HttpResponse("<p>" + str(t0) + "</p>")
