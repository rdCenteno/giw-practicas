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
    </tr>

    %for i in informacion:
    <tr>
        <td>{{i[0]}}</td>
        <td>{{i[1]}}</td>
        <td>{{i[2]}}</td>
        <td>{{i[4]}} Caduca:{{i[5]}}-{{i[6]}}</td>
        <td>{{i[3]}}</td>
        <td>{{i[7]}}</td>
        <td>{{i[8]}}</td>
        <td>{{i[9]}} {{i[10]}} {{i[11]}} {{i[12]}}</td>
        <td>{{i[13]}}</td>
    </tr>
	%end

    </table>


    <form action="/index">
    	<input type="submit" value="Volver al inicio" />
	</form>

</body>
</html>
