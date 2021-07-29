from django.conf.urls import url
from counting_cars import views

urlpatterns = [
    url(r'^cars/$', views.carsApi),
    url(r'^upload/$', views.carsUpload)
]