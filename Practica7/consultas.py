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

@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&surname=Romero&birthdate=2006-08-14


@get('/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31


@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc


@get('/find_birth_month')
def find_birth_month():
    # http://localhost:8080/find_birth_month?month=abril


@get('/find_likes_not_ending')
def find_likes_not_ending():
    # http://localhost:8080/find_likes_not_ending?ending=s


@get('/find_leap_year')
def find_leap_year():
    # http://localhost:8080/find_leap_year?exp=20




###################################
# NO MODIFICAR LA LLAMADA INICIAL #
###################################
if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)
