from django.conf.urls import url
from admin.myNLP import views

urlpatterns = {
    url(r'imdb-process', views.imdb_process),
    url(r'naver-process', views.naver_process),
}