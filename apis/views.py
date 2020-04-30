from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import HttpResponseBadRequest, JsonResponse
from rest_framework.decorators import api_view
import pymysql

# Create your views here.



def get_mysql_connection():
    connection = pymysql.connect(host='maya-dev.cxb0ogdnnu26.ap-southeast-1.rds.amazonaws.com',  port=3306,  user='root', passwd='V^GJ)!7-y5gL,"]>', db='maya_db', charset='utf8mb4', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    return connection

def sql_data_select(sql, connection):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()

@api_view(["GET"])
def news(requests): 
    connection = get_mysql_connection()
    query = "select * from users_smartphones"
    data = sql_data_select(query, connection)

    new1 = "hello"
    
    return Response({
        "status": "success",
        'news': new1,
        'data': data
    })



@api_view(["GET"])
def inital(requests):     
    return Response({
        "status": "success",
        'news': "tareq proxy pass working",
    })




