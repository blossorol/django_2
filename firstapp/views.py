import json

from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from firstapp.models import User


def users(request):
    if request.method == "POST":
        json_body = request.body
        print(json_body)
        json_data = json.loads(json_body)
        name = json_data.get('username')
        email = json_data.get('email')
        u = User.objects.create(name=name,email=email)
        u.save()
    all_entries =serializers.serialize("json", User.objects.all())
    return HttpResponse(all_entries, "application/json")
