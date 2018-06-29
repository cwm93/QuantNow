# -*- coding: utf-8 -*-

from django.conf.urls import url
from apps.blockchain import views

app_name = 'blockchain'

urlpatterns = [
    url(r'^$',views.index),
]