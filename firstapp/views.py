import json

from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from firstapp.models import User
from django.views import View
from firstapp.models import Article
from firstapp.models import Account
from django.shortcuts import render, HttpResponse, redirect, reverse
from firstapp.models import Account








def users(request):
    if request.method == "POST":
        json_body = request.body
        print(json_body)
        json_data = json.loads(json_body)
        name = json_data.get('username')
        email = json_data.get('email')
        u = User.objects.create(name=name, email=email)
        u.save()
    all_entries = serializers.serialize("json", User.objects.all())
    return HttpResponse(all_entries, "application/json")


class IndexView(View):
    """首页"""

    def get(self, request):
        all_Article = Article.objects.all().order_by()
        return render(request, 'index.html', {'all_Article': all_Article})


def login(request):
    if request.method == 'POST':
        print("进入页面")
        email = request.POST['username']
        password = request.POST['password']
        corr_email = Account.objects.filter(email=email).first()
        print("获取到信息")
        if email == corr_email.email and password == corr_email.password:
            print('登录成功')
            return HttpResponse('登录成功')

    return render(request, './log_in.html')


def logon(request):
    return HttpResponse('留作练习')


def logout(request):
    return HttpResponse('退出')


def index(request):
    print("进入index")
    return redirect(reverse('login'))
