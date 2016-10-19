from django.http import HttpResponse

from moviefun.models import *

# 数据库操作
def testdb(request):
	t1 = Movie(title = 'Title',
		year = 'Year',
		rated = 'Rated',
		released = 'Released',
		runtime = 'Runtime',
		genre = 'Genre',
		director = 'Director',
		writer = 'Writer',
		actors = 'Actors',
		plot = 'Plot',
		language = 'Language',
		awards = 'Awards',
		poster = 'Poster',
		#metascore = 'Metascore',
		imdbrating = 'imdbRating',
		imdbvotes = 'imdbVotes',
		imdbid = 'imdbID',
		type = 'Type')
	t1.save()
	return HttpResponse("<p>数据添加成功！</p>")
