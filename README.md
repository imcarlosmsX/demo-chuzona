# demo-chuzona
demo de la app chuzona.


La aplicación te pide un nombre y una dirección, que debe ser cercana al restaurante (ciudad de Barranquilla).

Luego muestra un menú de opciones para elegir el plato que se prefiera.

El domicilio se calcula a razón de la dirección, es decir, dependiendo de la distancia quer exista entre ésta dirección y la del restaurante,
que ya está predefinida.




##GUÍA para los archivos .json

settings.json: 

En la parte de "coords" se deben establecer las coordenadas del restaurante. LATITUD Y LONGITUD.


En la parte de "domis" se configura el precio del domicilio, según la distancia de la siguiente manera:

Pocisión [0]: Menor o igual a 1 KM de distancia.
Pocisión [1]: Entre 1KM y 5KM de distancia.
Pocisión [2]: Entre 5KM y 7KM de distancia.
Pocisión [3]: Entre 7KM y 10KM de distancia.
Pocisión [4]: Entre 10KM y 15KM de distancia.

En la parte de "ciudad" se configura la ciudad donde se encuentra el restaurante, como se indica en el ejemplo.


menu.json: 

Se trata de un diccionario que permite configurar el menú del restaurante.

La KEY va a ser el número que debe digitar el usuario. Las otras posiciones cumplen la siguiente función:

0. Nombre del plato.
1. Precio.
3. Descripción del plato
4. Número del plato.


