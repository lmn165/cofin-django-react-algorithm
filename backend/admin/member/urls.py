from django.conf.urls import url

from admin.member import views

urlpatterns = [
    url(r'^join', views.users),    # 가입, 전체조회, 수정
    url(r'^list', views.users),    # 전체조회
    url(r'^modify', views.users),    # 전체조회
    url(r'^login', views.login),
    url(r'^remove/(?P<username>\w{0,50})/$', views.remove),        # url path param을 받는 경우 ( ex) delete, find )
    url(r'^detail/(?P<username>\w{0,50})/$', views.detail),        # url path param을 받는 경우 ( ex) delete, find )
    # url(r'^/delete/<slug[-\w]>', views.users),        # url path param을 받는 경우 ( ex) delete, find )
]


'''
CBV 방식 (Class Based View)
from django.conf.urls import url
from .views import Members as members
from .views import Member as member
from django.urls import path, include
urlpatterns = [
    url('/register', members.as_view()),
    path('/<int:pk>/', member.as_view()),
]
'''