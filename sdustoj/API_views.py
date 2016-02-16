from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from sdustoj.models import *
import operator
import time
import json
import config
import os
import re
import datetime
from django.core import serializers
import shutil
from django.utils.timezone import utc
import operator

__author__ = 'Lonely'

'''
this page is the views about API
the url like /API/xxxx
'''

def API(request):
    c=RequestContext(request)
    return render_to_response('API/API.html',c)


def API_getprobleminfo(request):
    c=RequestContext(request)
    problems=Problem.objects.all()
    result=[]
    for item in problems:
        cache={}
        cache['problem_id']=item.problem_id
        cache['title']=item.title
        cache['memory_limit']=item.memory_limit
        cache['time_limit']=item.memory_limit
        result.append(cache)
    json_data = json.dumps(result)
    return HttpResponse(json_data,c)

def API_getsolutioninfo(request):
    c=RequestContext(request)
    user_id = ''
    result=[]
    try:
        if 'user' in request.GET:
            user_id=request.GET.get('user')
            solutions=Statusinfo.objects.filter(user_id=user_id)
            for item in solutions:
                cache={}
                cache['problem_id']=item.problem_id
                cache['memory']=item.memory
                cache['solution_id']=item.solution_id
                cache['time']=item.time
                cache['language']=item.language_name
                cache['status']=item.status
                cache['code_length']=item.code_length
                cache['contest_id']=item.contest_id
                result.append(cache)
    except Exception,e:
        pass
    #json_data = serializers.serialize("json", list(result))
    json_data=json.dumps(result)
    return HttpResponse(json_data,c)