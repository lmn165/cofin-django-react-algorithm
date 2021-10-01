from django.conf.urls import url

from admin.member import views

urlpatterns = [
    url(r'register', views.users),
    url(r'list', views.users)
]