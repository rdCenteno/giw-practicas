# -*- coding: utf-8 -*-

## -----------------------------------------------------------------------------
## Gestión de la información en la web. (GIW)
## Práctica 1
## Grupo 8
##
## AUTORES: Arturo Aguirre Calvo, Ignacio Vitores Sancho y Alberto Moreno Gracia
## declaramos:
## que esta solución es fruto exclusivamente de nuestro trabajo personal. No
## hemos sido ayudados por ninguna otra persona ni hemos obtenido la solución
## de fuentes externas, y tampoco hemos compartido nuestra solución con nadie.
## Declaramos además que no hemos realizado de manera deshonesta ninguna otra
## actividad que pueda mejorar nuestros resultados ni perjudicar los resultados
## de los demás.
## -----------------------------------------------------------------------------

# Incluir los 'import' necesarios
from bottle import route, run, get, post, template, request, redirect
from pymongo import MongoClient

def conectar_db():
     mongoclient = MongoClient()
     db = mongoclient['giw']
     return db

@get('/index')
def index():
    return '''
        <FORM ACTION="/index" METHOD="post">
        <br><br><br>
        <INPUT TYPE="radio" NAME="ejercicio" VALUE="find_users" CHECKED>1. find_users<br>
        <INPUT TYPE="radio" NAME="ejercicio" VALUE="find_email_birthdate" UNCHECKED>2. find_email_birthdate<br>
        <INPUT TYPE="radio" NAME="ejercicio" VALUE="find_country_likes_limit_sorted" UNCHECKED>3. find_country_likes_limit sorted<br>
        <INPUT TYPE="radio" NAME="ejercicio" VALUE="find_birth_month" UNCHECKED>4. find_birth_month<br>
        <INPUT TYPE="radio" NAME="ejercicio" VALUE="find_likes_not_ending" UNCHECKED>5. find_likes_not_ending<br>
        <INPUT TYPE="radio" NAME="ejercicio" VALUE="find_leap_year" UNCHECKED>6. find_leap_year<br> <br> <br>
        <INPUT VALUE="OK" TYPE="submit" />
        </FORM>
    '''

@route('/index', method='POST')
def redirecionar():
    ruta = request.forms.get('ejercicio')
    redirect("/" + ruta)


@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&surname=Romero&birthdate=2006-08-14

    info = []
    #Con el request.query se devuelve un diccionario que contiene los atributos de la url
    parametros = request.query
    db = conectar_db()
    c = db['users']
    res = c.find(parametros)
    for p in res:
        info.append([p["_id"], p["email"], p["webpage"], p["password"], p["credit_card"]["number"],             p["credit_card"]["expire"]["year"], p["credit_card"]["expire"]["month"], p["name"], p["surname"], p["address"]["country"], p["address"]["zip"], p["address"]["street"], p["address"]["num"], p["likes"]])

    return template('res_ej1.tpl', informacion=info)


@get('/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31
    return '''<h3>Ejercicio 2</h3>'''

@get('/index/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    return '''<h3>Ejercicio 3</h3>'''

@get('/find_birth_month')
def find_birth_month():
    # http://localhost:8080/find_birth_month?month=abril
    return '''<h3>Ejercicio 4</h3>'''

@get('/find_likes_not_ending')
def find_likes_not_ending():
    # http://localhost:8080/find_likes_not_ending?ending=s
    return '''<h3>Ejercicio 5</h3>'''

@get('/find_leap_year')
def find_leap_year():
    # http://localhost:8080/find_leap_year?exp=20
    return '''<h3>Ejercicio 6</h3>'''



###################################
# NO MODIFICAR LA LLAMADA INICIAL #
###################################
if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)











