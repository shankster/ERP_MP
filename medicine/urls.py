from django.conf.urls import url

from . import views

app_name = 'medicine'

urlpatterns = [
    url(r'^medicine', views.index, name='index'),
]