 <!DOCTYPE html>
<html lang="es">
<head>
<title>Servicio 1</title>
<meta charset="utf-8" />
</head>

<body>
    <header>

    </header>
    <FORM ACTION="/menuInicio/serv1/{{url}}" METHOD="post">
        <select name="web" disabled>
	  <option value={{url}}>{{url}}</option>
        </select>
	<select name="planta">
	%for planta in lista:
	  <option value={{planta}}>{{planta}}</option>
	%end
	</select>
        <INPUT VALUE="OK" TYPE="submit" />
    </form>

</body>
</html>


