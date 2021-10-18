from django.conf.urls import url

from admin.crawling import views

urlpatterns = {
    url(r'calculate', views.process),
}