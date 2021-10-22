from django.conf.urls import url
from admin.myCV2 import views

urlpatterns = {
    url(r'lena', views.lena),
    url(r'girl', views.girl),
    url(r'face-detect', views.face_detect),
    url(r'cat-mosaic', views.cat_mosaic),
    url(r'face-mosaic', views.face_mosaic)
}