from django.conf.urls import url

from admin.tensor import views

urlpatterns = {
    url(r'calculate', views.calculate),
    url(r'fashion', views.fashion)
}