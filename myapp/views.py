import time

from django.contrib import auth
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from myapp.models import User, Title
import json, re
from django.core.urlresolvers import reverse
from django import db
from django.contrib.auth import authenticate, login, logout

# Create your views here.


'''登录'''


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')

        password = request.POST.get('password')

        '''参数校验'''
        if not all([username, password]):
            pass
            # return redirect(reverse('users:login'))

        user = auth.authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


'''注册页面'''


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 获取参数：
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 校验参数
        if not all([username, password]):
            return redirect(reverse('register'))

        try:
            # todo 有所改动,看create用法
            # user = User.objects.create(name=username, password=password)
            user = User.objects.create_user(username=username, password=password)

        except db.IntegrityError:

            return render(request, 'register.html', {'errmsg': '用户已注册'})

        user.save()
        print(username, password)

        return redirect(reverse('index'))


'''主页展示'''


class Index(View):
    def get(self, request):

        user = request.user

        if user.is_authenticated():
            title = user.title_set.all().order_by('-create_time')
            context = {
                'user': user,
                'title': title
            }
            return render(request, 'index.html', context)

        else:
            return redirect(reverse('login'))


'''发布页面'''


class Publish(View):
    def get(self, request):
        return render(request, 'publish.html')


'''写文章'''


class NewArtical(View):
    def post(self, request):
        body = request.body
        data = json.loads(bytes.decode(body))

        title = Title()
        title.headline = data['title']
        title.contents = data['content']

        user = request.user

        if user:

            title.user = user
            title.author = user.username
            # 当前时间
            # TODO 数据库时间不对,不是东八区,少8小时(已解决,在setting里改时区)
            localTime = time.localtime(time.time())
            title.create_time = time.strftime('%Y.%m.%d', localTime)
            title.save()

            return HttpResponse("发布成功")

        else:
            return redirect(reverse('login'))


'''文章详情'''


class Artical(View):
    def get(self, request):
        user = request.user

        id = request.GET.get('id')

        title = Title.objects.get(id=id)

        context = {
            'name': user.username,
            'title': title
        }

        return render(request, 'artical.html', context)


class Logout(View):
    def get(self, request):
        logout(request)

        return redirect(reverse('login'))
