 <!DOCTYPE html>
<html lang="es">
<head>
<title>Ejercicio 1</title>
<meta charset="utf-8" />
</head>

<body>
<table>
    <tr>
        <td><strong>Usuario</strong></td>
        <td><strong>e-mail</strong></td>
        <td><strong>Página web</strong></td>
        <td><strong>Tarjeta de crédito</strong></td>
        <td><strong>Contraseña (hash)</strong></td>
        <td><strong>Nombre</strong></td>
        <td><strong>Apellido</strong></td>
        <td><strong>Dirección</strong></td>
        <td><strong>Aficiones</strong></td>
	<td><strong>Fecha de nacimiento</strong></td>
    </tr>
    %contador = 0
    %for i in informacion:
    %contador+=1
    <tr>
        <td>{{i[0]}}</td>
        <td><a href={{i[1]}}>{{i[1]}}</a></td>
        <td><a href={{i[2]}}>{{i[2]}}</a></td>
        <td>{{i[4]}} Caduca:{{i[5]}}-{{i[6]}}</td>
        <td>{{i[3]}}</td>
        <td>{{i[7]}}</td>
        <td>{{i[8]}}</td>
        <td>{{i[9]}} {{i[10]}} {{i[11]}} {{i[12]}}</td>
        <td>
	    %for j in i[13]:
	     %j = j.encode("UTF8")
	     {{j}} &nbsp
	    %end
	</td>
	<td>
	{{i[14]}}
	</td>
    </tr>
	%end
    <tr>
     Numero de resultados: {{contador}}
    </tr>
    </table>

</body>
</html>
