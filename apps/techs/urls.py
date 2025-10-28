from django.urls import path
from . import views

app_name = 'techs'

urlpatterns = [
    path('', views.tech_list, name='list'),
]
