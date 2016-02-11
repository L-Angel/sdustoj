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
import  shutil
from django.utils.timezone import utc
__author__ = 'Lonely'
powers=['A','B','C']
#must not use these words!
reserved=['null']

def admin_control(request):
    c=RequestContext(request)
    uname=''
    power=''
    if 'uname' in request.COOKIES:
        uname=request.COOKIES.get('uname')
    if 'power' in request.COOKIES:
        power=request.COOKIES.get('power')
    if power == 'A' or power == 'B':
        return HttpResponseRedirect(request.path,c)
    else :
        return HttpResponseRedirect('login',c)

def Login(request, user=None, u="", p=""):
    c=RequestContext(request)
    if 'uname' in request.POST:
        u = request.POST.get('uname')
    if 'pw' in request.POST:
        p = request.POST.get('pw')
    try:
        user = Users.objects.get(user_id=str(u))

    except Users.DoesNotExist:
        return render_to_response('Sign/signin.html',c)
    finally:
        if p!="" and str(p) == str(user.password) and len(p) > 0:
            result = 'true'
        else:
            result = 'false'
    if result == 'true':
        response = HttpResponseRedirect('index',c)
        response.set_cookie('uname', u, 3600)
        response.set_cookie('pw', p, 3600)
        response.set_cookie('power',user.defunct,3600)
        return response
    else:
        return render_to_response('Sign/signin.html',c)

def index(request):
    c=RequestContext(request)
    return render_to_response('index/index.html',c)

def user(request):
    c=RequestContext(request)
    userid=''
    login=False
    if 'uname' in request.GET:
        userid=request.GET.get('uname')
    if 'uname' in request.COOKIES:
        userid = request.COOKIES['uname']
        login=True
    user = Users.objects.filter(user_id=userid)[0]
    problemlist=Statusinfo.objects.filter(user_id=userid,status='Accepted').values('problem_id').distinct().order_by('problem_id')
    solve = len(problemlist)
    submit=len(Statusinfo.objects.filter(user_id=userid))
    ac=len(Statusinfo.objects.filter(user_id=userid,status='Accepted'))
    pe=len(Statusinfo.objects.filter(user_id=userid,status='Presentation Error'))
    wa=len(Statusinfo.objects.filter(user_id=userid,status='Wrong Answer'))
    tle=len(Statusinfo.objects.filter(user_id=userid,status='Time Limit Exceeded'))
    mle=len(Statusinfo.objects.filter(user_id=userid,status='Memory Limit Exceeded'))
    ole=len(Statusinfo.objects.filter(user_id=userid,status='Output Limit Exceeded'))
    re=len(Statusinfo.objects.filter(user_id=userid,status='Runtime Error'))
    ce=len(Statusinfo.objects.filter(user_id=userid,status='Compiler Error'))
    return render_to_response('user/user.html',{'user':user,'submit':submit,'ac':ac,'pe':pe,'wa':wa,'tle':tle,'mle':mle,'ole':ole,'re':re,'ce':ce,'solve':solve,'problemlist':problemlist,'login':login},c)


def useredit(request):
    c=RequestContext(request)
    userid= ''
    user=''
    if 'uname' in request.COOKIES:
        userid=request.COOKIES['uname']
        user = Users.objects.filter(user_id=userid)[0]
    return render_to_response('user/useredit.html',{'user':user},c)


def problem(request):
    c=RequestContext(request)
    islogin = False
    uname=''
    if 'uname' in request.COOKIES:
        uname=request.COOKIES.get('uname')
    if uname != '':
        islogin = True
    pid=request.GET.get('id')
    contestid=request.GET.get('contestid')
    problem=Problem.objects.filter(problem_id=pid)
    return render_to_response('problemset/problem.html',{'problem':problem[0],'islogin':islogin,'contestid':contestid},c)


def problemset(request):
    c=RequestContext(request)
    page_num=1
    if 'page_num' in request.GET:
        page_num = request.GET.get('page_num')
    problemlist=Problem.objects.all().order_by('problem_id')
    p=Paginator(problemlist,config.page_count)
    page=p.page_range
    if len(page) == 0:
        page=[1]
    problemlist=p.page(page_num).object_list
    cur_page=page_num
    return render_to_response('problemset/problemset.html',{'problemlist':problemlist,'page':page,'cur_page':cur_page},c)


def submit(request):
    c=RequestContext(request)
    contestid=-1
    if 'c_id' in request.GET:
        contestid = request.GET.get('c_id')
    problemid = request.GET.get('p_id')
    language=Language.objects.all()
    return render_to_response('problemset/submit.html',{'problemid':problemid,'language':language,'contestid':contestid},c)


def faq(request):
    c=RequestContext(request)
    return render_to_response('FAQ/faq.html',c)


def about(request):
    c=RequestContext(request)
    return render_to_response('Other/about.html',c)


def sign(request):
    c=RequestContext(request)
    return render_to_response('Sign/sign.html',c)


def signup(request):
    c=RequestContext(request)
    return render_to_response('Sign/signup.html',c)


def save(request):
    c=RequestContext(request)
    uname=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    rpwd=request.POST.get('rpwd')
    email=request.POST.get('email')
    validate=request.POST.get('validate')
    nick=request.POST.get('nick')
    ip=request.META.get('REMOTE_ADDR',None)
    if uname == '' or pwd == '' or nick == '':
        return render_to_response("Sign/signup.html",{'error':2},c)
    if pwd == rpwd:
        c_u=Users.objects.filter(user_id=uname)
        if c_u:
           return render_to_response("Sign/signup.html",{'error':3},c)
        u=Users(defunct='C',nick=nick,user_id=uname,password=pwd,email=email,volume=str(555),language=str(555),ip=str(ip),activated=str(555),submit=0,solved=0)
        u.save()
        return HttpResponseRedirect('index')
    else :
        return render_to_response("Sign/signup.html",{'error':1},c)

def signin(request):
    c=RequestContext(request)
    return render_to_response('Sign/signin.html',c)

def status(request):
    c=RequestContext(request)
    page_num = 1
    contest_id=-1
    if 'page_num' in request.GET:
        page_num = int(request.GET.get('page_num'))
    if 'op' in request.GET:
        op=request.GET.get('op')
        if '+' in str(op):
            page_num = page_num +1
        if '-' in str(op) and page_num > 1:
            page_num = page_num - 1
    if 'c_id' in request.GET:
        contest_id=request.GET.get('c_id')
        if contest_id != -1 and contest_id != None and contest_id != 'None':
            statusinfo=Statusinfo.objects.filter(contest_id=contest_id).order_by('-solution_id')
        else:
            statusinfo = Statusinfo.objects.all().order_by('-solution_id')
    else:
        statusinfo = Statusinfo.objects.all().order_by('-solution_id')
    p=Paginator(statusinfo,config.page_count)
    statusinfo=p.page(page_num).object_list
    page = p.page_range
    if len(page) >= 1:
        if page_num != page[-1]:
           page_num = page[-1]
    return render_to_response('Status/status.html',{'statusinfo':statusinfo,'cur_page':page_num},c)


def contest(request):
    c=RequestContext(request)
    uname=''
    power=''
    if 'uname' in request.COOKIES:
        uname=request.COOKIES.get('uname')
    if 'uname' in request.COOKIES:
        power=request.COOKIES.get('power')
    contestid = request.GET.get('id')
    problem_list = ContestProblem.objects.filter(contest_id=contestid).order_by('problem_id').values('contest_id','id','problem_id','title','num')
    for item in problem_list:
        status=Statusinfo.objects.filter(user_id=uname,problem_id=item['problem_id'],contest_id=item['contest_id'])
        if len(status) > 0:
            item['status']='Y'
        else :
            item['status']='N'
    contest = Contestinfo.objects.get(contest_id=contestid)
    cur_time=time.strftime('%Y-%m-%d %H:%M %p',time.localtime())
    if contest.privilege=='Private' and power != 'A':
        users=ContestUsers.objects.filter(contest_id=contestid,user_id=uname)
        if len(users) <= 0:
            return render_to_response('error/errorinfo.html',{'error':'contestprivilegeerror'},c)
    c_time=int(time.mktime(time.localtime()))
    s_time=int(time.mktime(contest.start_time.timetuple()))
    e_time=int(time.mktime(contest.end_time.timetuple()))
    if c_time < s_time:
        return render_to_response('error/errorinfo.html',{'error':'conteststarterror'},c)
    if c_time > e_time:
        return render_to_response('error/errorinfo.html',{'error':'contestfinisherror'},c)

    return render_to_response('contest/contest.html',{'problemlist':problem_list,'contest':contest,'cur_time':cur_time},c)


def contestlist(request):
    c=RequestContext(request)
    page_num = 1
    if 'page_num' in request.GET:
        page_num = request.GET.get('page_num')
        if page_num <= 0:
            page_num = 1
    contestlist=Contestinfo.objects.all().order_by('-contest_id').values('contest_id','title','start_time','end_time','defunct','points','privilege','language')
    for item in contestlist:
        cur_time=int(time.mktime(time.localtime()))
        s_time=int(time.mktime(item['start_time'].timetuple()))
        e_time=int(time.mktime(item['end_time'].timetuple()))
        if cur_time < s_time :
            status = 'Wating...'
        elif cur_time > e_time:
            status='Finished'
        elif cur_time >= s_time and cur_time <= e_time:
            status = 'Running'
        item['status']=status
    p=Paginator(contestlist,config.page_count)
    contestlist=p.page(page_num).object_list
    page=p.page_range
    if len(page) <= 0:
        page = [1]
    return render_to_response('contest/contestlist.html',{'contestlist':contestlist,'page':page,'cur_page':page_num},c)


def ranklist(request):
    c=RequestContext(request)
    page_num = 1
    if 'page_num' in request.GET:
        page_num = int(request.GET.get('page_num'))
    if 'op' in request.GET:
        op=request.GET.get('op')
        if '+' in str(op):
            page_num = page_num +1
        if '-' in str(op) and page_num > 1:
            page_num = page_num - 1
    users=Users.objects.all().values('nick','user_id')
    for user in users:
        user_id=user['user_id']
        user['ac']=ac=len(Statusinfo.objects.filter(status='Accepted',user_id=user_id))
        user['sub']=sub=len(Statusinfo.objects.filter(user_id=user_id))
        try:
            user['rate']=rate=str(ac*100.0/sub)+'%'
        except:
            user['rate']='0.0%'
    users.order_by('ac')
    count=1
    for user in users:
        user['index']=count
        count+=1
    p=Paginator(users,config.page_count)
    users=p.page(page_num).object_list
    page = p.page_range
    page = [1]
    if len(page) >= 1:
        if page_num != page[-1]:
            page_num = page[-1]
    return render_to_response('ranklist/ranklist.html',{'users':users,'cur_page':page_num},c)

def webboard(request):
    return render_to_response('webboard/webboard.html')

def admin(request):
    c=RequestContext(request)
    return render_to_response('admin/admin.html',c)


def sub_source(request):
    c=RequestContext(request)
    username = ''
    if 'uname' in request.COOKIES:
        username=request.COOKIES['uname']
    contestid=request.POST.get('c_id')
    problemid=request.POST.get('p_id')
    languageid = request.POST.get('language')
    source = request.POST.get('source')
    if contestid == None or contestid == '' or contestid == 'None' :
       contestid = -1
    if problemid == None or problemid == '' or problemid == 'None':
       problemid = -1
    s = Solution(problem_id=int(problemid),user_id=username,contest_id=int(contestid),language=int(languageid),result=0,code_length=len(source),time=0,memory=0,in_date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    s.save()
    s=s.solution_id
    sou=SourceCode(solution_id=s,source=source)
    sou.save()
    problem=Problem.objects.get(problem_id=problemid)
    problem.submit+=1
    problem.save()
    user=Users.objects.get(user_id=username)
    user.submit=user.submit+1
    user.save()
    return HttpResponseRedirect('status?c_id='+str(contestid),c)

def admin_login(request):
    c=RequestContext(request)
    return render_to_response("admin/login.html",c)


def admin_login_deal(request):
    c=RequestContext(request)
    user_name=''
    pwd=''
    if 'user_name' in request.POST:
        user_name = request.POST.get('user_name')
    if 'password' in request.POST:
        pwd = request.POST.get('password')
    if user_name != '':
        try:
            user = Users.objects.get(user_id=user_name)
            if str(user.password) == pwd:
                if user.defunct != 'C':
                    response=HttpResponseRedirect('index?menuName=&submenuName=See%20SDUSTOJ',c)
                    response.set_cookie('uname',user_name,3600)
                    response.set_cookie('power',user.defunct,3600)
                    return response
                else :
                    return render_to_response('admin/login.html',{'user_error':True},c)
            else:
                return render_to_response('admin/login.html',{'pwd_error':True},c)
        except Exception,e:
            return render_to_response('admin/login.html',{'user_error':True},c)
    else:
        return render_to_response('admin/login.html',{'user_error':True},c)

def admin_index(request):
    return render_to_response('admin/index.html')

def admin_addproblem(request):
    return render_to_response('admin/addproblem.html')


def admin_addproblem_save(request):
    c=RequestContext(request)
    title=request.POST.get('title')
    timelimit=request.POST.get('timelimit')
    memlimit=request.POST.get('memlimit')
    descripe=request.POST.get('descripe')
    input=request.POST.get('input')
    output=request.POST.get('output')
    sampleinput=request.POST.get('sampleinput')
    sampleoutput=request.POST.get('sampleoutput')
    hint=request.POST.get('hint')
    try:
        problem=Problem(in_date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),accepted=0,submit=0,solved=0,time_limit=timelimit,sample_output=sampleoutput,sample_input=sampleinput,title=title,memory_limit=memlimit,input=input,output=output,description=descripe,hint=hint)
        problem.save()

    except:
        return HttpResponse("failure",c)
    return HttpResponse("success",c)


def admin_addcontest(request):
    language=Language.objects.all()
    privilege=ContestPrivilege.objects.all();
    return render_to_response("admin/addcontest.html",{'language':language,'privilege':privilege})


def admin_addcontest_save(request):
    c=RequestContext(request)
    flag=True
    title=request.POST.get('title')
    starttime=request.POST.get('starttime')
    endtime=request.POST.get('endtime')
    contest_private=request.POST.get('contest_private')
    language=request.POST.get('language')
    problems=request.POST.get('problems')
    users=request.POST.get('users')
    c=Contest(defunct='C',title=title,start_time=datetime.datetime.strptime(starttime,'%Y-%m-%d %H:%M:%S').replace(tzinfo=utc),end_time=datetime.datetime.strptime(endtime,'%Y-%m-%d %H:%M:%S').replace(tzinfo=utc),private=int(contest_private),langmask=int(language))
    c.save()
    contestid=c.contest_id
    for problem in re.split(';|,',str(problems)):
        try:
            if problem != '':
                item=Problem.objects.get(problem_id=problem)
                cp=ContestProblem(contest_id=contestid,title=item.title,problem_id=item.problem_id,num=0)
                cp.save()
        except Exception,e:
            flag=False
    for user in re.split(';|,',str(users)):
        try:
            if user!='':
                item = Users.objects.get(user_id=user)
                cu=ContestUsers(user_id=user,contest_id=contestid,num=0)
                cu.save()
        except Exception,e:
            flag=False
    if flag==True:
        return HttpResponse("success",c)
    return HttpResponse("error",c)

def compileerror(request):
    c=RequestContext(request)
    solution_id=''
    if 'solution_id' in request.GET:
        solution_id=request.GET.get('solution_id')
    compileinfo = Compileinfo.objects.get(solution_id=solution_id)
    return render_to_response('error/errorinfo.html',{'error':'compileerror','compileerror':compileinfo.error},c)

def admin_problemlist(request):
    c=RequestContext(request)
    page_num = 1
    if 'page_num' in request.GET:
        page_num = int(request.GET.get('page_num'))
    if 'op' in request.GET:
        op=request.GET.get('op')
        if '+' in str(op):
            page_num = page_num +1
        if '-' in str(op) and page_num > 1:
            page_num = page_num - 1
    problems=Problem.objects.all().order_by('problem_id')
    p=Paginator(problems,config.admin_page_cuont)
    problems=p.page(page_num).object_list
    page = p.page_range
    if len(page) <=0:
        page = [1]
    if len(page) >= 1:
        if page_num != page[-1]:
            page_num = page[-1]
    return render_to_response('admin/problemlist.html',{'problems':problems,'cur_page':page_num,'totalpage':page[-1]},c)


def admin_addproblemfile(request):
    c=RequestContext(request)
    problems=Problem.objects.all()
    return render_to_response('admin/addproblemfile.html',{'problems':problems},c)


def admin_addproblemfile_save(request):
    c=RequestContext(request)
    files=request.FILES.getlist('files')
    problem_id=request.POST.get('problem_id')
    data_path=config.data_dir+'/'+str(problem_id)
    problem=Problem.objects.filter(problem_id=problem_id)
    if len(problem) > 0:
        try:
            if not os.path.exists(data_path):
                os.mkdir(data_path)
            else:
                shutil.rmtree(data_path)
                os.mkdir(data_path)
            for f in files:
                destination = open(data_path+'/'+f.name,'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            problem=problem[0]
            problem.fileupload='Y'
            problem.save()
            return render_to_response('admin/addproblemfile.html',{'result':'success'},c)
        except:
            return render_to_response('admin/addproblemfile.html',{'result':'failure'},c)
    return render_to_response('admin/addproblemfile.html',{'result':'failure'},c)


def admin_contestlist(request):
    c=RequestContext(request)
    page_num = 1
    if 'page_num' in request.GET:
        page_num = int(request.GET.get('page_num'))
    if 'op' in request.GET:
        op=request.GET.get('op')
        if '+' in str(op):
            page_num = page_num +1
        if '-' in str(op) and page_num > 1:
            page_num = page_num - 1
    contests=Contestinfo.objects.all().order_by('-contest_id')
    p=Paginator(contests,config.admin_page_cuont)
    contests=p.page(page_num).object_list
    page = p.page_range
    if len(page) <=0:
        page = [1]
    if len(page) >= 1:
        if page_num != page[-1]:
            page_num = page[-1]
    return render_to_response('admin/admin_contestlist.html',{'contests':contests,'cur_page':page_num,'totalpage':page[-1]},c)

def admin_newslist(request):
    c=RequestContext(request)
    page_num = 1
    if 'page_num' in request.GET:
        page_num = int(request.GET.get('page_num'))
    if 'op' in request.GET:
        op=request.GET.get('op')
        if '+' in str(op):
            page_num = page_num +1
        if '-' in str(op) and page_num > 1:
            page_num = page_num - 1
    news=News.objects.all().order_by('-news_id')
    p=Paginator(news,config.admin_page_cuont)
    news=p.page(page_num).object_list
    page = p.page_range
    if len(page) <=0:
        page = [1]
    if len(page) >= 1:
        if page_num != page[-1]:
            page_num = page[-1]
    return render_to_response('admin/newslist.html',{'news':news,'cur_page':page_num,'totalpage':page[-1]},c)

def admin_adduser(request):
    return render_to_response('admin/adduser.html')

def admin_addnews(request):
    c=RequestContext(request)
    return render_to_response('admin/addnews.html',c)

def admin_dealnews(request):
    c=RequestContext(request)
    op=request.POST.get('op')
    news_id=request.POST.get('news_id')
    if op == 'del':
        try:
            news=News.objects.get(news_id=news_id)
            news.delete()
        except Exception,e:
            return HttpResponse('failure',c)
    if op == 'release':
        release=request.POST.get('release')
        try:
            news = News.objects.get(news_id=news_id)
            news.release=int(release)
            news.save()
        except Exception,e:
            return HttpResponse('failure',c)
    return HttpResponse('success',c)



def admin_addnews_save(request):
    c=RequestContext(request)
    type=''
    release=''
    content=''
    author=''
    if 'type' in request.POST:
        type=request.POST.get('type')
    if 'type' in request.POST:
        release=request.POST.get('release')
    if 'type' in request.POST:
        content=request.POST.get('content')
    if 'uname' in request.COOKIES:
        author = request.COOKIES.get('uname')
    try:
        news = News(type=type,release=release,comment=content,author=author,time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        news.save()
        return HttpResponse('success',c)
    except Exception,e:
        return HttpResponse('failure',c)

def admin_getnews(request):
    c=RequestContext(request)
    type=request.POST.get('type')
    if int(type) == 0:
        news = News.objects.filter(type=0,release=1)
        str="["
        for item in news:
            str+='{\"content\":\"'+item.comment+'\"},'
        if len(str) <=1:
            str=str+']'
        else:
            str=str[0:-1]+']'
        return HttpResponse(str,c)
    if int(type) == 1:
        news = News.objects.filter(type=1,release=1)
        str="["
        for item in news:
            str+='{\"content\":\"'+item.comment+'\"},'

        if len(str) <=1:
            str=str+']'
        else:
            str=str[0:-1]+']'
        return HttpResponse(str,c)

def admin_userlist(request):
    c=RequestContext(request)
    page_num = 1
    if 'page_num' in request.GET:
        page_num = int(request.GET.get('page_num'))
    if 'op' in request.GET:
        op=request.GET.get('op')
        if '+' in str(op):
            page_num = page_num +1
        if '-' in str(op) and page_num > 1:
            page_num = page_num - 1
    users=Users.objects.all().order_by('user_id')
    p=Paginator(users,config.admin_page_cuont)
    users=p.page(page_num).object_list
    page = p.page_range
    if len(page) <=0:
        page = [1]
    if len(page) >= 1:
        if page_num != page[-1]:
            page_num = page[-1]
    return render_to_response('admin/userlist.html',{'users':users,'cur_page':page_num,'totalpage':page[-1]},c)

#---------------
def loginout(request):
    response=HttpResponseRedirect('index')
    response.delete_cookie("uname",path="/")
    response.delete_cookie("username",path="/")
    response.delete_cookie("power",path="/")
    return response

#-------------JSON

def getcodeinfo(request):
    c=RequestContext(request)
    solution_id=-1
    if 's_id' in request.POST:
        solution_id=request.POST.get('s_id')
    try:
        code=SourceCode.objects.get(solution_id=int(solution_id))
        code=str(code.source)
        code=re.sub("[\\\]",'\\\\',code)
        code=re.sub('\"','\\"',code)
        code=re.sub('[<]','&lt;',code)
        code=re.sub('[>]','&gt;',code)
        code=re.sub('[\r\n]','<p>',code)
        json_data='{\"source\":\"'+code+'\"}';
        return HttpResponse(json_data,c)
    except Exception,e:
        solution_id=-1
        return HttpResponse("{}",c)


def admin_deal_data(request):
    c=RequestContext(request)
    type=request.POST.get('type')
    if type == 'problem':
        try:
            problem_id=request.POST.get('p_id')
            ppath=config.data_dir+"/"+problem_id
            if os.path.exists(ppath):
                shutil.rmtree(ppath)
            problem=Problem.objects.get(problem_id=problem_id)
            problem.delete()
        except Exception,e:
            return HttpResponse("{\"result\":\"failure\"}",c)
    elif type == 'contest':
        try:
            contest_id=request.POST.get('c_id')
            contest=Contest.objects.get(contest_id=contest_id)
            contest.delete()
        except Exception,e:
            return HttpResponse("{\"result\":\"failure\"}",c)
    elif type == 'user':
        try:
            user_id=request.POST.get('u_id')
            user=Users.objects.get(user_id=user_id)
            user.delete()
        except Exception,e:
            return HttpResponse("{\"result\":\"failure\"}",c)
    return HttpResponse("{\"result\":\"success\"}",c)

def admin_dealuser(request):
    c=RequestContext(request)
    pwd=request.POST.get('pwd')
    uname=request.POST.get('uname')
    power=request.POST.get('power')
    try:
        user=Users.objects.get(user_id=uname)
        if pwd not in reserved:
            user.password=pwd
        if power in powers:
            user.defunct=power
        user.save()
    except Exception,e:
        return HttpResponse("{\"result\":\"failure\"}",c)
    return HttpResponse("{\"result\":\"success\"}",c)



