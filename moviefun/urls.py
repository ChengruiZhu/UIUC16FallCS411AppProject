
from django.conf.urls import url

from . import views
from . import insert
from . import update
from . import select1
from . import select2
from . import select3
from . import insert_all
from . import insert_loc
from . import insert_ll
#from . import delete_all
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^post/(?P<lat_1>\f+&P<lat_2>\f+&P<log_1>\f+&P<log_2>\f+)/$',
    #     views.post_detail, name='post_detail'),
    url(r'^post/(?P<id>\d+)/$',
        views.post_detail, name='post_detail'),
    #url(r'test',testdb.testdb),
    url(r'insert/',insert.insert),
    url(r'update/',update.update),
    url(r'select1/', select1.select),
    url(r'select2/', select2.select),
    url(r'select3/', select3.select),
    url(r'create',insert_all.insert_all),
    url(r'location',insert_loc.insert_loc),
    url(r'address',insert_ll.insert_ll),
    #url(r'delete_all',delete_all.delete_all),
]
