from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Account


# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, 'account/register.html')

    elif request.method == "POST":
        id = request.POST.get('id', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}
        if not (id and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            res_data['success'] = "회원가입이 완료되었습니다."
            user = Account(id=id, password=make_password(password), birth="2019-01-01", gender="남자")
            user.save()
        return render(request, 'account/register.html', res_data)
