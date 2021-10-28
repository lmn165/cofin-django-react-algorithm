from django.conf.urls import url

from admin.member import views

urlpatterns = [
    url(r'/user', views.users, name='users'),    # 가입, 전체조회, 수정
    url(r'/login', views.login, name='login'),
    url(r'/?P<slug[-\w]>', views.users),        # url path param을 받는 경우 ( ex) delete, find )
]