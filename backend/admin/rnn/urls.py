from django.conf.urls import url
from admin.rnn import views

urlpatterns = {
    url(r'ram-price', views.ram_price)
}