# ikb/urls.py
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'ikb'
urlpatterns = [
    url(r'^$', views.add, name='add'),
    # path('index/', views.add, name='add'),
]
