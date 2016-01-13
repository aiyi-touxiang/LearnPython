from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 在这儿编写视图
# home_page = None


def home_page(request):
    return render(request, 'home.html')
