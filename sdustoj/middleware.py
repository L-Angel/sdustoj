from django.http import HttpResponseRedirect
from urllib import quote
import re
class QtsAuthenticationMiddleware(object):
    def process_request(self,request):
        if request.path!='/admin/login' and request.path != '/admin/admin_login_deal' and request.path.count('/') == 2:
            power=''
            if 'power' in request.COOKIES:
                power = request.COOKIES.get('power')
            if power == 'A' or power =='B':
                pass
            else :
                return HttpResponseRedirect('login')