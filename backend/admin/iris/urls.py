from django.conf.urls import url

from admin.iris import views

urlpatterns = {
    url(r'base', views.base),
    url(r'advanced', views.advanced),
    url(r'iris-by-tf', views.iris_by_tf)
}
