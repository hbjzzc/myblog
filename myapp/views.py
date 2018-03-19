import time
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from myapp.models import User, Title
import json, re
from django.core.urlresolvers import reverse
from django import db
from django.contrib.auth import authenticate, login

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

        user = User.objects.filter(name=username).first()

        if (user):

            if user.password == password:
                request.session['name'] = username
                return redirect('index')

            else:
                return render(request, 'login.html', {'errmsg': '密码错误'})

        else:
            return render(request, 'login.html', {'errmsg': '用户不存在'})


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
            user = User.objects.create(name=username, password=password)

        except db.IntegrityError:

            return render(request, 'register.html', {'errmsg': '用户已注册'})

        user.save()
        print(username, password)

        return HttpResponse('注册成功')


'''主页展示'''


class Index(View):
    def get(self, request):
        username = request.session.get('name')

        user = User.objects.filter(name=username).first()

        title = user.title_set.all()

        context = {
            'user': user,
            'title': title
        }
        return render(request, 'index.html', context)


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

        username = request.session.get('name')
        user = User.objects.filter(name=username).first()
        title.user = user

        title.author = username
        # 当前时间
        # TODO 数据库时间不对,不是东八区,少8小时(已解决,在setting里改时区)
        localTime = time.localtime(time.time())
        title.create_time = time.strftime('%Y.%m.%d', localTime)
        title.save()

        print(type(title.create_time))

        return HttpResponse("发布成功")


'''文章详情'''


class Artical(View):
    def get(self, request):

        username = request.session.get('name')

        id = request.GET.get('id')

        title = Title.objects.get(id=id)

        context = {
            'name':username,
            'title': title,
        }

        return render(request, 'artical.html', context)
