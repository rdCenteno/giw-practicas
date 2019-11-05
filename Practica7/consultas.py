# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Gestión de la información en la web. (GIW)
# Práctica 1
# Grupo 8
##
# AUTORES: Arturo Aguirre Calvo, Ignacio Vitores Sancho y Alberto Moreno Gracia
# declaramos:
# que esta solución es fruto exclusivamente de nuestro trabajo personal. No
# hemos sido ayudados por ninguna otra persona ni hemos obtenido la solución
# de fuentes externas, y tampoco hemos compartido nuestra solución con nadie.
# Declaramos además que no hemos realizado de manera deshonesta ninguna otra
# actividad que pueda mejorar nuestros resultados ni perjudicar los resultados
# de los demás.
# -----------------------------------------------------------------------------

# Incluir los 'import' necesarios
from bottle import route, run, get, post, template, request, redirect
from pymongo import MongoClient


def conectar_db():
    mongoclient = MongoClient()
    db = mongoclient['giw']
    return db


def devuelveValores(objeto):
    return [objeto["_id"], objeto["email"], objeto["webpage"], objeto["password"], objeto["credit_card"]["number"], objeto["credit_card"]["expire"]["year"],
            objeto["credit_card"]["expire"]["month"], objeto["name"], objeto["surname"], objeto[
                "address"]["country"], objeto["address"]["zip"], objeto["address"]["street"],
            objeto["address"]["num"], objeto["likes"], objeto["birthdate"]]


@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&surname=Romero&birthdate=2006-08-14
    parametrosValidos = {"name": "", "surname": "", "birthdate": ""}
    parametrosErroneos = {}
    # Con el request.query se devuelve un diccionario que contiene los atributos de la url
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
        info = []
        for resultado in res:
            info.append(devuelveValores(resultado))
        return template('res_ej1.tpl', informacion=info)
    else:
        # Mostrar error
        error = "Los siguientes parametros no son validos:  "
        for parametro in parametrosErroneos:
            error += parametro + "=" + parametrosErroneos[parametro] + "  "
        return error


@get('/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31
    parametrosValidos = {"from": "", "to": ""}
    parametros = request.query
    for parametro in parametros:
            parametrosValidos[parametro] = parametros[parametro]
    db = conectar_db()
    c = db['usuarios']
    res = c.find({"birthdate": {"$gte": parametrosValidos["from"], "$lte": parametrosValidos["to"]}})
    info = []
    # Falta por hacer la plantilla y coger los resultados
    for resultado in res:
        info.append(devuelveValores(resultado))
    return template('res_ej1.tpl', informacion=info)

@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    parametrosValidos = {"country": "", "likes": "", "limit": "", "ord": ""}
    parametros = request.query
    for parametro in parametros:
        parametrosValidos[parametro] = parametros[parametro]
    parametrosValidos["likes"] = parametrosValidos["likes"].split(",")
    if parametrosValidos["ord"] == "asc":
        parametrosValidos["ord"] = 1
    else:
        parametrosValidos["ord"] = -1
    db = conectar_db()
    c = db['usuarios']
    res = c.find({ "address.country":parametrosValidos["country"], "likes": {"$all": parametrosValidos["likes"]}}).limit(parametrosValidos["limit"]).sort("birthdate",parametrosValidos["ord"])
    info = []
    # Falta por hacer la plantilla y coger los resultados
    for resultado in res:
        info.append(devuelveValores(resultado))
    return template('res_ej1.tpl', informacion=info)
    


@get('/find_birth_month')
def find_birth_month():
    # http://localhost:8080/find_birth_month?month=abril
    diccionarioMeses = {"enero":"-01-","febrero":"-02-","marzo":"-03-","abril":"-04-","mayo":"-05-","junio":"-06-","julio":"-07-","agosto":"-08-","septiembre":"-09-","octubre":"-10-","noviembre":"-11-","diciembre":"-12-"}
    mes = request.query["month"]
    db = conectar_db()
    c = db['usuarios']
    res = c.find({"birthdate":{"$regex":diccionarioMeses[mes]}}).sort("birthdate")
    info = []
    for resultado in res:
        info.append(devuelveValores(resultado))
    return template('res_ej1.tpl', informacion=info)


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
    run(host='localhost', port=8080, debug=True)
