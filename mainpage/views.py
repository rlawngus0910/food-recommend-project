from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.db import connection
from django.template import context


def indexView(request):
    if request.method == 'GET':
        try:
            cursor = connection.cursor()
            SQL = "SELECT A.id,A.restaurant_id,A.title,A.comment,A.user_id,B.name FROM post A, restaurant B WHERE A.restaurant_id = B.id ORDER BY id DESC LIMIT 4"
            cursor.execute(SQL)
            datas = cursor.fetchall()

            connection.commit()
            connection.close()

            posts = []

            for data in datas:
                row = {'id' : data[0],
                       'restaurant_id' : data[1],
                       'title' : data[2],
                       'comment' : data[3],
                       'user_id' : data[4],
                       'name' : data[5]}

                posts.append(row)

        except:
            connection.rollback()


        return render(request, 'mainpage/index.html',{'posts' : posts})

    elif request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password', None)

        try:
            cursor = connection.cursor()
            SQL = "SELECT id, password FROM accounts WHERE id = %s"

            cursor.execute(SQL, [id])
            user = cursor.fetchall()

            connection.commit()

            if not user:
                return render(request, 'mainpage/index.html', {"message" : "존재하지 않는 아이디입니다."})

            userId = user[0][0]
            userPassword = user[0][1]

            if check_password(password, userPassword):
                postSQL = "SELECT A.id,A.restaurant_id,A.title,A.comment,A.user_id,B.name FROM post A, restaurant B WHERE A.restaurant_id = B.id ORDER BY id DESC LIMIT 4"

                cursor.execute(postSQL)
                datas = cursor.fetchall()

                connection.commit()
                connection.close()

                posts = []

                for data in datas:
                    row = {'id': data[0],
                           'restaurant_id': data[1],
                           'title': data[2],
                           'comment': data[3],
                           'user_id': data[4],
                           'name': data[5]}

                    posts.append(row)

                request.session['user'] = userId
                return render(request, 'mainpage/index.html',{'posts' : posts})  # 로그인 성공

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
