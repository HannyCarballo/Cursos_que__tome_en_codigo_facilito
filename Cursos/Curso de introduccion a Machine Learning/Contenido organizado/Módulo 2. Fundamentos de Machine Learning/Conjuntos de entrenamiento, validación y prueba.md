# Conjuntos de entrenamiento, validación y prueba
Una vez que tenemos los ejemplos para entrenar un modelo de machine learning, una de las primeras tareas que hay que llevar a cabo es de dividir nuestro conjunto de ejemplos en tres subconjuntos distintos.

### Dividiendo el dataset
- Set de entrenamiento
- Set de validación
- Set de prueba
Tanto el conjunto de validación como el de prueba se les conoce como conjuntos "ocultos", la razon de estos conjuntos es que cuando entrenamos un modelo de ML esperamos que sea bueno en un conjunto de datos que no ha visto o sobre el cual no ha sido entrenado.

### Conjunto de entrenamiento
Es el conjunto más grande, su proposito es el de ser usado por el algoritmo para entrenar y producir el modelo.

### Conjunto de validación
También conocido como el conjunto de desarrollo, es usado por el desarrollador para decidir que modelo usar.

### Conjunto de pruebas
Usado para medir que tan bueno es el modelo entrenado, este se debe usar para la toma de decisiones.

### Tamaño ideal de los conjuntos
Una de las grandes preguntas que no se han resuelto es ¿cómo es que nosotros decidimos el tamaño ideal de los conjuntos?. La verdad es que no hay una respuesta clara y depende de muchos factores.
<p align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89166148/172971760-b38f2567-9336-474c-a74c-20074369dc48.png">
</p>

A continuación, se presenta una pequeña guia de como dividir la información.
<p align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89166148/172971928-dee2c35b-dd89-463e-8165-1d3b5850cf15.png">
</p>

Cuando no se tiene una cantidad suficiente de información, suele suceder que el conjunto de validación es omitido, favoreciendo otras técnicas, como por ejemplo, la validación cruzada.
<p align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89166148/172972184-1d57ef78-9ff2-4997-825d-4e54d0100ddd.png">
</p>
