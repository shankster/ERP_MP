from django.conf.urls import url

from . import views

app_name = 'supplier'

urlpatterns = [
    url(r'^supplier', views.index, name='index')

]