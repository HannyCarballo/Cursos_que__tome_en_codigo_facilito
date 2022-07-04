# El DNS y su funcionamiento
Primero, el navegador recibe nuestra solicitud para por ejemplo, google.com
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/173477299-c57ea192-8c8b-46d2-a030-8402489b0096.png">
</p>

El navegador con la intención de no molestar a otros, busca en sus registros a los que llamaremos el cache, para saber en que dirección IP está google.com
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/173477299-c57ea192-8c8b-46d2-a030-8402489b0096.png">
</p>

Estos registros se actualizan cada que registramos un sitio web, para que la segunda vez no tengamos que hacer todo el recorrido de busqueda. Si el navegador no encuentra en sus registros del cache el IP correspondiente a google.com, le preguntará al sistrema operativo.
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/173477299-c57ea192-8c8b-46d2-a030-8402489b0096.png">
</p>

El sistema operativo buscará en su propio cache o en sus propios registros, para saber si ya conoce cual es la IP para dicha página. En caso de que tampoco esta 
