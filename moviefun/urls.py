
from django.conf.urls import url

from . import views
from . import testdb
from . import insert_all

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'test',testdb.testdb),
    url(r'insert',insert_all.insert),
]
