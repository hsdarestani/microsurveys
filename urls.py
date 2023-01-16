# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from .views import *
app_name = "microsurveys"
urlpatterns = [
    path('microsurveys/SubAns', SubAns, name='SubAns'),
]
