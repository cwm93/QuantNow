# -*- coding: utf-8 -*-
"""
电影票房
"""

from django.conf.urls import url
from apps.box_office import views

app_name = 'box_office'

urlpatterns = [
    url(r'^$',views.current_datetime),
]
