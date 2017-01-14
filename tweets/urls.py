from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.create_tweet, name='create_tweet'),
]