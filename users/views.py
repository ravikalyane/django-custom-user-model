from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()


def index(request):
    users = User.objects.all().values_list('id', 'username', 'full_name')
    return HttpResponse('<script>setTimeout(3000, alert("hi"))</script>')
