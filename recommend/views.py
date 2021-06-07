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
        if size == '컸으면 좋겠다':
            SQL = "SELECT id, name, menu, location, category FROM restaurant WHERE area > 150 LIMIT 5"
        else:
            SQL = "SELECT id, name, menu, location, category FROM restaurant WHERE area <= 150 LIMIT 5"

        cursor.execute(SQL)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        restaurants = []

        for data in datas:
            row = {'id' : data[0],
                   'name' : data[1],
                   'menu' : data[2],
                   'location' : data[3],
                   'category' : data[4]}

            restaurants.append(row)

    except:
        connection.rollback()
    return render(request, 'recommend/service.html', {'restaurants' : restaurants})
