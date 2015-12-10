from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from sdustoj.models import *
import json

__author__ = 'Lonely'


@csrf_exempt
def Login(request, user=None, u="", p=""):

    if 'uname' in request.POST:
        u = request.POST.get('uname')
    if 'pw' in request.POST:
        p = request.POST.get('pw')
    try:
        user = Users.objects.get(user_id=str(u))

    except Users.DoesNotExist:
        return render_to_response('Sign/signin.html')
    finally:
        if str(p) == str(user.password) and len(p) > 0:
            result = 'true'
        else:
            result = 'false'
    print(result)
    if result == 'true':
        response = render_to_response('index/index.html')
        response.set_cookie('uname', u, 3600)
        response.set_cookie('pw', p, 3600)
        return response
    else:
        return render_to_response('Sign/signin.html')


def index(request):
    return render_to_response('index/index.html')


def user(request):
    return render_to_response('user/user.html')


def useredit(request):
    return render_to_response('user/useredit.html')


def problem(request):
    return render_to_response('problemset/problem.html')


def problemset(request):
    return render_to_response('problemset/problemset.html')


def submit(request):
    return render_to_response('problemset/submit.html')


def faq(request):
    return render_to_response('FAQ/faq.html')


def about(request):
    return render_to_response('Other/about.html')


def sign(request):
    return render_to_response('Sign/sign.html')


def signup(request):
    return render_to_response('Sign/signup.html')

def signin(request):
    return render_to_response('Sign/signin.html')


def status(request):
    return render_to_response('Status/status.html')


def contest(request):
    return render_to_response('contest/contest.html')


def contestlist(request):
    return render_to_response('contest/contestlist.html')


def ranklist(request):
    return render_to_response('ranklist/ranklist.html')
