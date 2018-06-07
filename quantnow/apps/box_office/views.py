# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import datetime

# Create your views here.

def index(request):
    return HttpResponse('box_office index!')

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('box_office/datetime.html')
    html = t.render({'current_date':now})
    return HttpResponse(html)

def test(request):
    return render_to_response('share_layout/base.html')