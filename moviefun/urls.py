
from django.conf.urls import url

from . import views
#from . import testdb
from . import insert_all
from . import delete_all
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'test',testdb.testdb),
    url(r'insert',insert_all.insert),
    url(r'delete',delete_all.delete_all),
]
