from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import *
import cx_Oracle


# Create your views here.

def index(request):
    config = settings.DATABASES["default"]
    connection = cx_Oracle.connect("%s/%s@%s" % (config["USER"], config["PASSWORD"], config["NAME"]))
    cursor = connection.cursor()

    response = cursor.execute("SELECT * FROM USERS").fetchall()
    text = "Usuarios: "
    for i in response:
        text += str(i)
    connection.close()
    return HttpResponse(text)


def insert_example(request):
    config = settings.DATABASES["default"]
    connection = cx_Oracle.connect("%s/%s@%s" % (config["USER"], config["PASSWORD"], config["NAME"]))
    cursor = connection.cursor()

    phones = Phone(('31983516161'))
    address = Address(501,'14','Promissão II','Lagoa Santa', "a", "a", "a")

    matheus = User("Matheus de Jesus", "matheus@matheus", "matheuzinhoGameplay", address, phones, "senha")
    my_query = "INSERT INTO USERS (" + matheus.get_format() + ")"
    my_query += " VALUES (" + matheus.get_values() + ")"

    cursor.execute(my_query)
    connection.commit()
    connection.close()
    return HttpResponse("Inserção feita")
