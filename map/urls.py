from django.conf.urls import url
from map import views

urlpatterns = [
    url(r'^', views.maps, name='maps'),
]

