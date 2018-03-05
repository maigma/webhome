from django.conf.urls import url
from maps import views

urlpatterns = [
    url(r'^', views.maps, name='maps'),
]

