# con muchas líneas de código
calificacion = 10
color = None
if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

print(calificacion, color)

# con pocas líneas de código, gracias al operador ternario
calificacion = 5
# cuando estamos condicionando en una sola línea de código el else se vuelve obligatorio
color = 'Verde' if calificacion >=7 else 'Rojo' 
print(calificacion, color)