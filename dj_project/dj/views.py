from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    # return HttpResponse("hello Django")
    return render(request, 'index.html')

def login_action(request):
    if request.method == 'POST':
        user = request.POST.get('user','')
        passwd = request.POST.get('passwd','')
        #  新增部分
        username = auth.authenticate(username=user, password=passwd)  # 不通过
        # if user == 'admin' and passwd == 'admin':
        if username is not None:
            auth.login(request, username)   # 登录
            # return HttpResponse('login success!')
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', user, 3600)     # 添加浏览器cookie
            request.session['user'] = user                 # 添加浏览器session，报错：'WSGIRequest' object has no attribute 'session'
            return response
        else:
            return render(request, 'index.html', {'error':'username or password error!','user':user,'passwd':passwd})
@login_required
def event_manage(request):
    '''登录成功后的页面管理'''
    # user = request.COOKIES.get('user','')   # 读取浏览器cookie
    user = request.session.get('user','')      # 读取浏览器session
    return render(request, "event_manage.html", {"user": user})