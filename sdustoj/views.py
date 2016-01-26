from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from sdustoj.models import *
import time
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
        if p!="" and str(p) == str(user.password) and len(p) > 0:
            result = 'true'
        else:
            result = 'false'
    print(result)
    if result == 'true':
        response = render_to_response('index/index.html')
        response.set_cookie('uname', u, 3600)
        response.set_cookie('pw', p, 3600)
        response.set_cookie('power',user.defunct,3600)
        return response
    else:
        return render_to_response('Sign/signin.html')

def index(request):
    return render_to_response('index/index.html')

def user(request):
    userid=''
    if 'uname' in request.GET:
        userid=request.GET.get('uname')
    if 'uname' in request.COOKIES:
        userid = request.COOKIES['uname']
    print userid
    user = Users.objects.filter(user_id=userid)[0]
    problemlist=Statusinfo.objects.filter(user_id=userid).values('problem_id').distinct().order_by('problem_id')
    solve = len(problemlist)
    print solve
    submit=len(Statusinfo.objects.filter(user_id=userid))
    ac=len(Statusinfo.objects.filter(user_id=userid,status='Accepted'))
    pe=len(Statusinfo.objects.filter(user_id=userid,status='Presentation Error'))
    wa=len(Statusinfo.objects.filter(user_id=userid,status='Wrong Answer'))
    tle=len(Statusinfo.objects.filter(user_id=userid,status='Time Limit Exceeded'))
    mle=len(Statusinfo.objects.filter(user_id=userid,status='Memory Limit Exceeded'))
    ole=len(Statusinfo.objects.filter(user_id=userid,status='Output Limit Exceeded'))
    re=len(Statusinfo.objects.filter(user_id=userid,status='Runtime Error'))
    ce=len(Statusinfo.objects.filter(user_id=userid,status='Compiler Error'))
    return render_to_response('user/user.html',{'user':user,'submit':submit,'ac':ac,'pe':pe,'wa':wa,'tle':tle,'mle':mle,'ole':ole,'re':re,'ce':ce,'solve':solve,'problemlist':problemlist})


def useredit(request):
    userid= ''
    user=''
    if 'uname' in request.COOKIES:
        userid=request.COOKIES['uname']
        user = Users.objects.filter(user_id=userid)[0]
    return render_to_response('user/useredit.html',{'user':user})


def problem(request):
    pid=request.GET.get('id')
    contestid=request.GET.get('contestid')
    problem=Problem.objects.filter(problem_id=pid)
    return render_to_response('problemset/problem.html',{'problem':problem[0],'contestid':contestid})


def problemset(request):
    problemlist=Problem.objects.all().order_by('problem_id')
    return render_to_response('problemset/problemset.html',{'problemlist':problemlist})


def submit(request):
    contestid = request.GET.get('c_id')
    problemid = request.GET.get('p_id')
    return render_to_response('problemset/submit.html',{'problemid':problemid,'contestid':contestid})


def faq(request):
    return render_to_response('FAQ/faq.html')


def about(request):
    return render_to_response('Other/about.html')


def sign(request):
    return render_to_response('Sign/sign.html')


def signup(request):
    return render_to_response('Sign/signup.html')

@csrf_exempt
def save(request):
    uname=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    rpwd=request.POST.get('rpwd')
    email=request.POST.get('email')
    validate=request.POST.get('validate')
    nick=request.POST.get('nick')
    ip=request.META.get('REMOTE_ADDR',None)
    if uname == '' or pwd == '' or nick == '':
        return render_to_response("Sign/signup.html",{'error':2})
    if pwd == rpwd:
        c_u=Users.objects.filter(user_id=uname)
        if c_u:
           return render_to_response("Sign/signup.html",{'error':3})
        u=Users(user_id=uname,password=pwd,email=email,volume=str(555),language=str(555),ip=str(ip),activated=str(555))
        u.save()
        return HttpResponseRedirect('index')
    else :
        return render_to_response("Sign/signup.html",{'error':1})

def signin(request):
    return render_to_response('Sign/signin.html')

def status(request):
    statusinfo = Statusinfo.objects.all().order_by('-solution_id')
    return render_to_response('Status/status.html',{'statusinfo':statusinfo})


def contest(request):
    contestid = request.GET.get('id')
    problem_list = ContestProblem.objects.filter(contest_id=contestid).order_by('problem_id')
    contest = Contestinfo.objects.filter(contest_id=contestid)
    cur_time=time.strftime('%Y-%m-%d %H:%M %p',time.localtime())
    return render_to_response('contest/contest.html',{'problemlist':problem_list,'contest':contest[0],'cur_time':cur_time})


def contestlist(request):
    contestlist=Contestinfo.objects.all().order_by('-contest_id')
    return render_to_response('contest/contestlist.html',{'contestlist':contestlist})


def ranklist(request):
    return render_to_response('ranklist/ranklist.html')

def webboard(request):
    return render_to_response('webboard/webboard.html')

def admin(request):
    return render_to_response('admin/admin.html')

@csrf_exempt
def sub_source(request):
    username = ''
    if 'uname' in request.COOKIES:
        username=request.COOKIES['uname']
    contestid=request.POST.get('c_id')
    problemid=request.POST.get('p_id')
    language = request.POST.get('language')
    source = request.POST.get('source')
    if contestid == None or contestid == '' or contestid == 'None' :
       contestid = 0
    if problemid == None or problemid == '' or problemid == 'None':
       problemid = 0
    languageid = Language.objects.filter(language_name=language)
    try:
        languageid=languageid[0].language
    except :
        languageid = 1
    if  languageid == None or languageid == '':
        languageid = 1
    s = Solution(problem_id=int(problemid),user_id=username,contest_id=int(contestid),language=int(languageid),result=-1,code_length=len(source),in_date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    s.save()
    s=s.solution_id
    sou=SourceCode(solution_id=s,source=source)
    sou.save()
    return HttpResponseRedirect('status')

def admin_login(request):
    return render_to_response("admin/login.html")

def admin_login_deal(request):
    return HttpResponseRedirect('admin/index')

def admin_index(request):
    return render_to_response('admin/index.html')

def admin_addproblem(request):
    return render_to_response('admin/addproblem.html')

def admin_addproblem_save(request):
    return HttpResponse()