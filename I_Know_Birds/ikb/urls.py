# ikb/urls.py
from django.urls import path
from . import views

app_name = 'ikb'
urlpatterns = [
    path('index/', views.add, name='add'),
]
