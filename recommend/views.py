from django.shortcuts import render
from django.db import connection

# Create your views here.

def recommendView(request):
    return render(request, 'recommend/Q&A(1).html')

def recommendResultView(request):
    print(request.GET)
    price = request.GET['price']
    who = request.GET['who']
    time = request.GET['time']
    size = request.GET['size']

    try:
        cursor = connection.cursor()
        SQL = ""
        rateSQL = "SELECT ROUND(AVG(rate),2) FROM post WHERE restaurant_id = %s GROUP BY restaurant_id"

        if price == '허름하더라도 저렴한 곳':
            if size == '컸으면 좋겠다':
                SQL = "SELECT id, name, menu, location, category,price FROM restaurant WHERE price < 10000 AND area > 100 LIMIT 5"
            else:
                SQL = "SELECT id, name, menu, location, category,price FROM restaurant WHERE price < 10000 AND area <= 100 LIMIT 5"

        elif price == '비싸더라도 럭셔리한 곳':
            if size == '컸으면 좋겠다':
                SQL = "SELECT id, name, menu, location, category,price FROM restaurant WHERE price >= 10000 AND area > 100 LIMIT 5"
            else:
                SQL = "SELECT id, name, menu, location, category,price FROM restaurant WHERE price >= 10000 AND area <= 100 LIMIT 5"

        cursor.execute(SQL)
        datas = cursor.fetchall()

        connection.commit()

        restaurants = []
        rates = []

        for data in datas:
            cursor.execute(rateSQL, [data[0]])
            rateData = cursor.fetchall()

            if len(rateData) == 0:
                row = {'id': data[0],
                       'name': data[1],
                       'menu': data[2],
                       'location': data[3],
                       'category': data[4],
                       'rate': 0}

            else:
                row = {'id' : data[0],
                       'name' : data[1],
                       'menu' : data[2],
                       'location' : data[3],
                       'category' : data[4],
                       'rate' : rateData[0]}

            # rates.append(rateData)

            connection.commit()

            restaurants.append(row)

        print(restaurants)
    except:
        connection.rollback()
    return render(request, 'recommend/service.html', {'restaurants' : restaurants,'rates' : rates})

def detailView(request, id):
    cursor = connection.cursor()
    if request.method == "POST":
        title = request.POST.get('title')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user_id = request.session.get('user')

        print(user_id)

        try:
            SQL = "INSERT INTO post (title, comment, rate, restaurant_id, user_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(SQL, [title, comment, rating, id, user_id])

            connection.commit()
            connection.close()

        except:
            connection.rollback()

    try:
        cursor = connection.cursor()
        rateSQL = "SELECT ROUND(AVG(rate),2) FROM post WHERE restaurant_id = %s GROUP BY restaurant_id"
        SQL = "SELECT id, name, menu, location, category FROM restaurant WHERE id = %s"

        cursor.execute(SQL, [id])
        datas = cursor.fetchall()

        restaurants = []
        for data in datas:
            cursor.execute(rateSQL, [data[0]])
            rateData = cursor.fetchall()

            rateDataList = list(rateData)
            if len(rateData) == 0:
                row = {'id': data[0],
                       'name': data[1],
                       'menu': data[2],
                       'location': data[3],
                       'category': data[4],
                       'rate': 0}

            else:
                row = {'id': data[0],
                       'name': data[1],
                       'menu': data[2],
                       'location': data[3],
                       'category': data[4],
                       'rate': rateDataList[0]}

                print(type(rateData[0]))

            # rates.append(rateData)

            connection.commit()

            restaurants.append(row)

        connection.commit()

        print(restaurants[0])

        postSQL = "SELECT title, comment, rate, user_id FROM post WHERE restaurant_id = %s"
        cursor.execute(postSQL, [id])
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        posts = []

        for data in datas:
            row = {
                'title': data[0],
                'comment' : data[1],
                'rate' : data[2],
                'user_id' : data[3],
            }

            posts.append(row)

        print(posts)

    except:
        connection.rollback()

    return render(request, 'recommend/detail.html', {'restaurants' : restaurants[0], 'posts' : posts})

def recommendMenuView(request):
    if request.method == "GET":
        return render(request, 'recommend/menu.html')

    elif request.method == "POST":
        menu = request.POST.get('menu')
        print(menu)
        try:
            cursor = connection.cursor()
            rateSQL = "SELECT ROUND(AVG(rate),2) FROM post WHERE restaurant_id = %s GROUP BY restaurant_id"
            SQL = "SELECT id, name, menu, location, category FROM restaurant WHERE menu = %s LIMIT 10"

            cursor.execute(SQL, [menu])
            datas = cursor.fetchall()

            print(datas)

            restaurants = []

            for data in datas:
                cursor.execute(rateSQL, [data[0]])
                rateData = cursor.fetchall()

                if len(rateData) == 0:
                    row = {'id': data[0],
                           'name': data[1],
                           'menu': data[2],
                           'location': data[3],
                           'category': data[4],
                           'rate': 0}

                else:
                    row = {'id': data[0],
                           'name': data[1],
                           'menu': data[2],
                           'location': data[3],
                           'category': data[4],
                           'rate': rateData[0]}

                # rates.append(rateData)

                connection.commit()

                restaurants.append(row)

            connection.commit()
            connection.close()

        except:
            print('DB 오류')
            connection.rollback()

        return render(request, 'recommend/service.html', {'restaurants' : restaurants})