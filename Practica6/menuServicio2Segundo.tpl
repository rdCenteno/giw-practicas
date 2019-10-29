 <!DOCTYPE html>
<html lang="es">
<head>
<title>Servicio 2</title>
<meta charset="utf-8" />
</head>

<body>
    <header>

    </header>

    <FORM ACTION="/menuInicio/serv2p2" METHOD="post">
        <textarea name="palabras" rows="10" cols="50">{{palabras}}</textarea> <br>
        <INPUT TYPE="radio" NAME="tipo" VALUE="and" CHECKED> Búsqueda AND
        <INPUT TYPE="radio" NAME="tipo" VALUE="or" UNCHECKED> Búsqueda OR <br>
        <INPUT VALUE="Buscar" TYPE="submit" />
    </form>
	<br><br>
	<form action="/menuInicio">
    	<input type="submit" value="Volver al inicio" />
	</form>

</body>
</html>


