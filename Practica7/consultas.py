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

def devuelveValores(objeto):
    return [objeto["_id"], objeto["email"], objeto["webpage"], objeto["password"], objeto["credit_card"]["number"], objeto["credit_card"]["expire"]["year"], 
    objeto["credit_card"]["expire"]["month"], objeto["name"], objeto["surname"], objeto["address"]["country"], objeto["address"]["zip"], objeto["address"]["street"], 
    objeto["address"]["num"], objeto["likes"], objeto["birthdate"]] 
                



@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&surname=Romero&birthdate=2006-08-14
    parametrosValidos = {"name":"","surname":"","birthdate":""}
    parametrosErroneos = {}
    #Con el request.query se devuelve un diccionario que contiene los atributos de la url
    parametros = request.query
    for parametro in parametros:
        if parametro in parametrosValidos:
            parametrosValidos[parametro] = parametros[parametro]
        else:
            parametrosErroneos[parametro] = parametros[parametro]
    
    if not parametrosErroneos:
        db = conectar_db()
        c = db['usuarios']
        res = c.find(parametros)
        info=[]
        for resultado in res:
            info.append(devuelveValores(resultado))
        return template('res_ej1.tpl', informacion=info)
    else:
        #Mostrar error 
        error = "Los siguientes parametros no son validos:  "
        for parametro in parametrosErroneos:
            print(type(parametrosErroneos[parametro]))
            error += parametro + "=" + parametrosErroneos[parametro] + "  "
        return error

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











