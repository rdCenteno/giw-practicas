 <!DOCTYPE html>
<html lang="es">
<head>
<title>Servicio 3</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       
    </header>
    <FORM ACTION="/menuInicio/serv3" METHOD="POST">
	<h2>Selecciona la/s enfermedad/es:</h2>
    <table>
    %for fila in enfermedades:
     <tr>
    %for enfermedad in fila:
    <td>
	  <input name="enfermedades" type="checkbox" value={{enfermedad}}>{{enfermedad}}</option>
    </td>
%end
     </tr>
%end
    </table>
	
        <span><INPUT VALUE="OK" TYPE="submit" /> &nbsp &nbsp &nbsp</span>
    </form>

	<form action="/menuInicio">
    	<input type="submit" value="Volver al inicio" />
	</form>
	
</body>
</html>



