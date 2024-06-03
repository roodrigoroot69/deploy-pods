## EJERCICIO 3. Despliegue de Pods.

**Requisitos:**
- Desplegar 3 pods
	- FastApi

        - Desplegar app FastApi en el puero 8000 -> [Pods despleago](http://a450e27f95a1f4204be6c7c9831f96d8-327780230.us-east-2.elb.amazonaws.com:8000/ "Pods despleago")
		 
        - Endpoint que devuelva un mensaje JSON -> [Endpoint](http://a450e27f95a1f4204be6c7c9831f96d8-327780230.us-east-2.elb.amazonaws.com:8000/items/10 "Endpoint")

    - ReactJS:

		 [Despliegue de Pod y Accesible fuera del cluster mediante el LoadBalancer](http://accbf4a15c4e945689428d3511feace2-468035719.us-east-2.elb.amazonaws.com:3000/ "Despliegue de Pod y Accesible fuera del cluster mediante el LoadBalancer")

	- PostgreSQL

		- Despliegue de Pod  -> [PostgreSQL](http://padd724a8eff214e79b204af9183744f1-1982455500.us-east-2.elb.amazonaws.com "PostgreSQL") (No se muestra nada en el navegador, pero se podran conectar utilizando algún gestor como DBeaver)

    Accesible desde otro Pod dentro del Cluster -> Pod FastApi a PostgreSQL (Imagen):

![Conexión a la DB](https://github.com/roodrigoroot69/deploy-pods/blob/main/app/captura.jpg?raw=true "a title")



## Preguntas

**¿Cómo manejarías los secretos y variables de entorno sensibles en estos pods?**

Pudieramos utilizar secrets y SSM de AWS, para guardar ahí los secretos y variables y las definimos en el código de pulumi para obtener esos valores

**¿Qué estrategias utilizarías para escalar estos pods según la carga de trabajo?**
Se pueden utilizar estrategias de crecimiento vertical y horizontal

Horizontalmente: Aumentar los pods basado en el rendiminetos del CPU
Verticalmente: Aumentando la capacidad de los recursos de los pods



**¿Cómo realizarías el monitoreo y registro de estos pods en un entorno de producción?**

Podemos utilizar cloudwatch para ver los logs que se esten generando.
Tanto como los errores o algún mensaje que se necesite agregar, a su vez podemos configurar alertas para que notifiquen en caso de error o bien algún escenario en especifico.

Otra que también podemos usar es Sentry.io que también nos puede ayudar de la misma manera que cloudwatch, pero proporcinando incluso más contexto o apoyo con los errores

