from django.shortcuts import render,redirect
from qingShang.models import *
from hashlib import sha1
# Create your views here.
def register(request):
    return render(request,'register.html')
def register_handle(request):
    #接受用户输入
    post = request.POST
    uName = post.get('c')
    uPwd = post.get('pwd')
    uPwd2 = post.get('cpwd')
    uEmail = post.get('email')
    #判断两次密码
    if uPwd != uPwd2:
        return redirect('/qing/register/')
    #密码加密
    s1 = sha1()
    s1.update(uPwd.encode("utf8"))
    uPwd3 = s1.hexdigest()
    print(uName)
    #创建对象
    user = UserInfo()
    user.uName = uName
    user.uEmail = uEmail
    user.uPwd = uPwd3
    user.save()

    return redirect('/qing/login/')
def login(request):


    return render(request, 'login.html')
def login_handle(request):
    name = request.POST.get('username')
    pwd = request.POST.get('pwd')
    s1 = sha1()
    s1.update(pwd.encode("utf8"))
    pwd2 = s1.hexdigest()
    print(name)
    num = UserInfo.objects.filter(uName = 'yangyuwei').count()
    if num == 1:
        user = UserInfo.objects.get(uName=name)
        if user.uPwd == pwd2:
            return redirect('/qing/index/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def index(request):

    return render(request,'index.html')

def list(request):

    return render(request,'list.html')

