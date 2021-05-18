from django.shortcuts import render
from django.db import connection

def RestaurantListView(request):
    try:
        cursor = connection.cursor()

        SQL = "SELECT id, name FROM restaurant"
        result = cursor.execute(SQL)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        restaurants = []

        for data in datas:
            row = {'id' : data[0],
                   'name' : data[1]}

            restaurants.append(row)

    except:
        connection.rollback()

    return render(request, 'restaurants/restaurants_list.html', {'restaurants' : restaurants})