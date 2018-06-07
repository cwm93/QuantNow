# -*- coding: utf-8 -*-
"""
电影票房
"""

from django.conf.urls import url
import apps.box_office.views

app_name = 'box_office'

urlpatterns = [
    url(r'^$',apps.box_office.views.current_datetime),
]
