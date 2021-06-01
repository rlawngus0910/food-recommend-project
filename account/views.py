from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Accounts
from django.db import connection

# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, 'account/register3.html')

    elif request.method == "POST":
        id = request.POST.get('id')
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        email = request.POST.get('e-mail', None)
        nickname = request.POST.get('nickname', None)
        address = request.POST.get('address', None)
        birth = request.POST.get('birth', None)
        gender = request.POST.get('gender', None)

        res_data = {}

        if password != re_password:
            return render(request, 'account/register3.html', {"message" : "입력한 비밀번호가 다릅니다."})

        else:

            try:
                cursor = connection.cursor()
                password = make_password(password)
                SQL = "INSERT INTO accounts (id,password,email,nickname,address,birth,gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(SQL, [id, password, email, nickname, address, birth, gender])

                connection.commit()
                connection.close()
                return render(request, '../../mainpage/templates/mainpage/index.html', {"message" : "회원가입이 완료되었습니다."})

            except:
                connection.rollback()
                return render(request, 'account/register3.html', {"message" : "DB 오류 발생"})


