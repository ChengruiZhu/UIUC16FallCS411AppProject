from django.http import HttpResponse

from moviefun.models import *

# 数据库操作
def testdb(request):
	t1 = Movie.objects.filter(year='2007')
	response=''
	for var in t1:
		response += var.title
		response += '\r'
	return HttpResponse("<p>" + response + "</p>")
