from django.shortcuts import render
from django.db import connection

def indexView(request):
    return render(request, 'mainpage/index.html')