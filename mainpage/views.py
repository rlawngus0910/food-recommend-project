from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.db import connection
from django.template import context


def indexView(request):
    if request.method == 'GET':
        return render(request, 'mainpage/index.html')

    elif request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password', None)

        try:
            cursor = connection.cursor()
            SQL = "SELECT id, password FROM accounts WHERE id = %s"
            print(id)

            cursor.execute(SQL, [id])
            print(id)
            user = cursor.fetchall()

            connection.commit()
            connection.close()

            if not user:
                return render(request, 'mainpage/index.html', {"message" : "존재하지 않는 아이디입니다."})

            userId = user[0][0]
            userPassword = user[0][1]

            print(userId)
            print(userPassword)
            if check_password(password, userPassword):
                print('여기냐?1')
                request.session['user'] = userId
                print('여기냐?2')
                # context['userSession'] = request.session['user']
                print('여기냐?3')
                return render(request, 'mainpage/index.html')

            else:
                return render(request, 'mainpage/index.html', {"message" : "비밀번호가 일치하지 않습니다."})

        except:
            print('DB 오류')
            connection.rollback()

    return render(request, 'mainpage/index.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/mainpage')
