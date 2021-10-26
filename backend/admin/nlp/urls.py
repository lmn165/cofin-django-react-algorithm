from django.conf.urls import url
from admin.nlp import views

urlpatterns = {
    url(r'imdb-process', views.imdb_process),
    url(r'naver-process', views.naver_process),
}