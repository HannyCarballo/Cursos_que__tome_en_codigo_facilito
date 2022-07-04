# ¿Qué son las Container Queries?
Son una especificación que se introduce a CSS que nos permite aplicar condiciones sobre los valores de un elemento, esto es algo muy similar a lo que hacemos en media queries.

### Media queries
Las media queries nos permiten realizar consultas sobre los valores del viewport o información del dispositivo del usuario, y con base en estos valores nosotros podemos aplicar ciertos estilos condicionalmente.
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174668304-8a0a8519-78ef-48de-b8bb-d8c9f3ec99f8.png">
</p>

El viewport normalmente es el tamaño de la pantalla.
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174668522-61e9b4f3-6ef5-484d-b69f-27a933dd0ac9.png">
</p>

### Container queries
Los container queries en funciolnalidad son iguales a las media queries, la diferencia está en que los valores que podemos consultar pueden ser elementos que esten dentro de nuestra página web y no solamente valores del viewport.
En esta clase de escenarios, la representación del elemento depende del espacio que tenga disponible en donde ha sido colocado, y no depende de la pantalla del usuario:
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174669047-631062f0-f2f9-4895-a609-ff3cc090019c.png">
</p>

Los container queries requieren de dos declaraciones para funcionar:
- Definir un elemento contenedor.
- Definir reglas @container.

### Propiedad container
La propiedad container es un shorthand(una propiedad que me permite asignar el valor de varias propiedades) para definir los valores de las propiedades container-type y container-name.

### Container-type
Define un elemento como un contenedor query. Los hijos pueden consultar información de su tamaño, layout, estilo y estado.
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174670142-19f390d0-e069-4082-befb-5fded22a157d.png">
</p>

Los posibles valores de container-type son:
- size: Establece un contenedor query para hacer consultas sobre la dimensión de bloque e incline del elemento.
- inline-size: Establece un contenedor query para hacer consultas sobre la dimensión inline del contenedor.
- block-size: Establece un contenedor query para hacer consultas sobre la dimensión block del contenedor.
- style: Establece un contenedor query para hacer consultas sobre los estilos del contenedor.
- state: Establece un contenedor query para hacer consultas sobre el estado del contenedor.

### Container-name
Nos permite definir una lista de nombres para el contenedor para ser usados en la definición de la regla @container 
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174674934-5725a44f-db36-4477-9345-4f2ce5ef9e16.png">
</p>

### @container
Similar a la regla @media, la regla @container nos permite definir consultas sobre un elemento contenedor. La sintaxis es la siguiente:
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174675991-efdf5e4d-291a-493c-a123-5e57192e0374.png">
</p>

Algunos ejemplos son los siguientes:
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174676192-9ca0086d-b762-44e0-a585-d9691a63a2e6.png">
</p>

<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174676189-04f02bab-8765-4421-8315-468b39436920.png">
</p>

Es común que las reglas @container que definamos no incluyan el nombre de un contenedor.
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/174676616-aa717018-5784-4c78-a607-3f7f7247ee85.png">
</p>

Por defecto se usa el ancestro más cercano, esto quiere decir que para un elemento .card se buscará el ancestro más cercano que sea un elemento contenedor.

### En resumen
Para usar container queries debo:
- Definir un elemento contenedor
- Definir reglas @container
- Los estilos de @container se aplican al ancestro más cercano
