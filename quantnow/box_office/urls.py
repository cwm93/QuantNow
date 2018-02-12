# -*- coding: utf-8 -*-
"""
电影票房
"""

from django.conf.urls import url
import box_office.views

app_name = 'box_office'

urlpatterns = [
    url(r'^box_office/',box_office.current_datetime),
]
