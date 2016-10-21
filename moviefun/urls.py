
from django.conf.urls import url

from . import views
from . import testdb
from . import insert
from . import select1
from . import insert_all
from . import delete_all
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'test',testdb.testdb),
    url(r'insert',insert.insert),
    url(r'select', select1.select),
    #url(r'insert_all',insert_all.insert),
    #url(r'delete_all',delete_all.delete_all),
]
