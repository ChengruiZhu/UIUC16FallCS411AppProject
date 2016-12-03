
from django.conf.urls import url

from . import views
# from . import insert
from . import update
from . import select1
from . import select2
from . import select3
# from . import insert_all
# from . import insert_loc
# from . import insert_ll
from . import insert_recommendation
from . import checkrecommendation
#from . import delete_all
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get/(?P<lat_1>\d+\.\d+)/(?P<lat_2>\d+\.\d+)/(?P<log_1>\d+\.\d+)/(?P<log_2>\d+\.\d+)/$',views.post_detail, name='post_detail'),
    url(r'^like/(?P<imdbid>[a-z0-9]{9})/$',views.love, name='love'),
   # url(r'^post/(?P<id>\d+)/$',
    #    views.post_detail, name='post_detail'),
    #url(r'test',testdb.testdb),
    # url(r'insert/',insert.insert),
    url(r'update/',update.update),
    url(r'select1/', select1.select),
    url(r'select2/', select2.select),
    url(r'select3/', select3.select),
    # url(r'create',insert_all.insert_all),
    # url(r'location',insert_loc.insert_loc),
    # url(r'address',insert_ll.insert_ll),
    url(r'recommendation',insert_recommendation.insert_recommendation),
    url(r'check',checkrecommendation.checkrecommendation),
    #url(r'delete_all',delete_all.delete_all),
]
