lenguajes = 'Python Ruby Java Rust C++ C'
 
# método split. 
# funciona cuando hay espacios
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)
# se separa por carácter
lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-')
print(listado_lenguajes)
# especificar cuales queremos dividir el string
lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-', 2)
print(listado_lenguajes)

# método join. nos permite generar un string a partir de una lista
lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
string_lenguajes = ' '.join(lenguajes)
print(string_lenguajes)
string_lenguajes = '/'.join(lenguajes)
print(string_lenguajes)