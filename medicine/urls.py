from django.conf.urls import url

from . import views

app_name = 'medicine'

urlpatterns = [
    url(r'^', views.index, name='index'),
]