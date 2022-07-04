# Feature engineering

### Datos "crudos"
Usualmente cuando trabajamos en el mundo real, los datos que tomamos se consideran "crudos". Estos datos existen en su forma natural y no siempre son susceptibles de ser usados en esta forma para ML.
Algunos ejemplos sobre datos "crudos" son:
- Mediciones del clima.
- Imágenes de una cámara.
- Audio de grabadoras.
- Fechas del calendario.

### Los algoritmos funcionan con datos numéricos
<p align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89166148/172955474-c1fa874b-9a5a-4336-baa9-afec78d69ade.png">
</p>

Todos los algoritmos de aprendizaje automático funcionan unicamente con datos de tipo numérico. Por ejemplo, no podemos usar imágenes en JPG directamente como entradas para un algoritmo, sino que debemos que ejecutar un proceso conocido como ingeniería de características o feature engineering para extraer los valores de cada pixel de la imagen, estos valores son números, sobre los que ahora sí nuestro algoritmo elegido puede actuar y entrenar un modelo.
<p align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89166148/172956036-efe19833-00ec-4424-8ad6-c0ab719188ec.png">
</p>

Esto es muy comun en problemas con datos no estructurados, por ejemplo:
- Reconocimiento de voz- sampleo en frecuencias.
- Tratamiento de video- dividir en frames.
- Lenguaje natural- dividir en palabras.

Aunque sucede con datos estructurados también
- Variables categóricas, como la nacionalidad o el sexo deben ser transformadas.
- Tambien hay muchas formas de representar una fecha.

#### Ejemplos - características
<p align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89166148/172970569-e889bd5f-9743-4651-bb12-800f5140f69f.png">
</p>

### Feature engineering
- Proceso complejo
- Depende de muchos factores
- Ningún análisis se parece al otro
