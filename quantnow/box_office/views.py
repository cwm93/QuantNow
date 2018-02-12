# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import datetime

# Create your views here.

def datetime(request):
    now = datetime.datetime.now()
    t = get_template('datetime.html')
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)