from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CityView.as_view()),
    url(r'^getInfo/', views.getInfo),
]