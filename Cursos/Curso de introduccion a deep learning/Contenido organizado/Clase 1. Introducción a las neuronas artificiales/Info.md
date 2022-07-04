# Deep Learning

### ¿Por qué muchos problemas buscan resolverse con deep learning?
Por el simple hecho de que yo no tengo que definir de forma explicita para datos que sean muy complejos, que tengan relaciones ocultas, relaciones muy robustas, o datos que sean muy dificiles de comprender a ojo humano. 
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/175169982-c1080aa6-ecff-4c33-adcd-46e38da0a83e.png">
</p>

### Historia de las neuronas
En la historia de la humanidad las personas han hecho cosas increibles. A partir de observar fenomenos de la naturaleza, los seres humanos hemos buscado entender y replicar comportamientos naturales; en algun momento alguien vió un enjamble de abejas y pensó "las abejas siempre vuelan en grupos, los enjambles, y nunca chocan entre ellas", se sentó, empezó a modelar el comportamiento de las abejas y así es como surgen algoritmos de enjamble, que tienen muchas aplicaciones en drones, en su momento sucedió algo similar con las neuronas, trás entender el funcionamiento de la neurnoa dijeron "podríamos intentar crear un modelo que esté inspirado en como funciona la neurona en el cuerpo humano"
<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/89166148/175172262-8d106c7a-d4e8-4753-af97-548068cd84bc.png">
</p>

En este sentido de esta neurona, llevo a una neurona artificial.
<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/89166148/175173966-d16ac3d4-bedc-4eb2-b36f-3d0e82cda640.png">
</p>

### Bias y funciones de activación
Bias se traduce como sesgo. Lo siguiente se puede ver como una función matemática:
<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/89166148/175178391-1cebe6e0-0ed7-4069-b99a-ec980668576f.png">
</p>

Al momento de comparar lo puedo ver como una función matemática. Si yo tengo un vector de entradas y pesos, yo puedo también definir un umbral y si wjxj es menor al umbral devuelvo un  0, si wjxj es mayor al umbral devuelvo un 1. La función que se utiliza se llama función de activación porque la neurona recibe esta información y la procesa, la neurona se activa, eso significa que dispara la información o no, y eso significa que solo te va a devolver un 0; al ser una  función de activación , como en las matemáticas y en el universo existen una infinidad de funciones, eso significa que además no solamente podemos usar esta función, sino que podemos usar muchas más funciones, de hecho la función que más se utiliza es la función sigmoide.

### Redes neuronales y producto matricial
Consideremos la siguiente imagen...
<p align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/89166148/175181178-1bdfae0c-07f9-409c-87cb-73be3af69c79.png">
</p>

En este sentido, si yo me fijo solamente en una neurona, podría interpretar que la neurona está recibiendo dos datos de entrada, y esta neurona su salida la manda a otra neurona, así es como se componen las redes neuronales. Las redes neuronales las podemos pensar como capas de neuronas que transmiten esta información, a partir de los datos de entrada y devuelven las salidas.
- Producto matricial.
<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/89166148/175181730-3c29a035-e7ff-4331-a849-0d0e0e218e36.png">
</p>

Para multiplicar una matriz por otra, se debe cumplir que el número de columnas de la primera debe ser igual al número de columnas de la segunda.
<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/89166148/175182161-25e5c2d3-cfd8-41e2-a85e-b96566ce5dee.png">
</p>

<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/89166148/175182465-9a32702d-d60e-422d-acd6-567a1afa6a03.png">
</p>

### Red neuronal de pesos aleatorios
<p align="center">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/89166148/175182929-ba5fd321-d508-4d48-9470-d67a1664552c.png">
</p>

Con redes de este estilo, aunque las redes no hayan aprendido nada, podemos general imágenes muy interesantes de este estilo.


