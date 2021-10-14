from django.conf.urls import url

from admin.crime import views

urlpatterns = {
    url(r'crime-model', views.crime_model),
    url(r'police-position', views.police_position),
    url(r'cctv-model', views.cctv_model),
    url(r'population-model', views.population_model),
    url(r'merge-cctv-pop', views.merge_cctv_pop),
    url(r'sum-pol', views.sum_pol),
    url(r'process', views.process)
}