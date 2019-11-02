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
    redirect("/index/" + ruta)


@get('/index/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&surname=Romero&birthdate=2006-08-14
    return template('p_ej1.tpl')


@route('/index/find_users', method='POST')
def find_users():
    parametros = []
    resultados = []
    name = request.forms.get('name')
    surname = request.forms.get('surname')
    birthday = request.forms.get('birthday')
    if (name != ""):
        parametros.append(["name", name])
    if (surname != ""):
        parametros.append(["surname", surname])
    if (birthday != ""):
        parametros.append(["birthday", birthday])
    db = conectar_db()
    c = db['users']
    busqueda = "{"
    # Para concatenar los parametros que haya
    for i in parametros:
        busqueda = busqueda + '"' + i[0] + '":"' + i[1] + '",'
    # Quito la coma que sobra del final
    busqueda = busqueda[0:len(busqueda)-1]
    busqueda += "}"
    print(busqueda)
    # No funciona creo que porque no le vale que sea una variable
    # en vez de {"name":"Juan"}
    resultados = c.find(busqueda)
    for p in resultados:
        print(p)
        print("------------------------------")
    return '<p>Busqueda</p>'








@get('/index/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31
    return '''<h3>Ejercicio 2</h3>'''

@get('/index/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    return '''<h3>Ejercicio 3</h3>'''

@get('/index/find_birth_month')
def find_birth_month():
    # http://localhost:8080/find_birth_month?month=abril
    return '''<h3>Ejercicio 4</h3>'''

@get('/index/find_likes_not_ending')
def find_likes_not_ending():
    # http://localhost:8080/find_likes_not_ending?ending=s
    return '''<h3>Ejercicio 5</h3>'''

@get('/index/find_leap_year')
def find_leap_year():
    # http://localhost:8080/find_leap_year?exp=20
    return '''<h3>Ejercicio 6</h3>'''



###################################
# NO MODIFICAR LA LLAMADA INICIAL #
###################################
if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)











