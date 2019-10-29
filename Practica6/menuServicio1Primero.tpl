 <!DOCTYPE html>
<html lang="es">
<head>
<title>Servicio 1</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       
    </header>
    <FORM ACTION="/menuInicio/serv1" METHOD="post">
        <select name="web">
	%for web in webs:
	  <option value={{web}}>{{web}}</option>
	%end 
        </select>
	<select name="planta" disabled>
	  <option value="">-- PLANTA --</option>
	</select>
        <INPUT VALUE="OK" TYPE="submit" />
    </form>

	<form action="/menuInicio">
    	<input type="submit" value="Volver al inicio" />
	</form>
	
</body>
</html>



