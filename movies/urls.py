from django.conf.urls import url
from . import views


urlpatterns = [
      
      url(r'^$', views.movies, name='movies'),
      url(r'^movie/(\d+)', views.youtube, name = 'netflix'),
]
