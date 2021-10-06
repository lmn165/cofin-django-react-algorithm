from django.conf.urls import url

from admin.crime import views

urlpatterns = {
    url(r'crime-model', views.crime_model),
    url(r'police-position', views.police_position)
}