#2. Escribir un programa que lea nombres de la consola hasta que se introduzca un 0 y
#calcule el total de caracteres que se han introducido. que se han introducido.

caracteres = 0
nombre = ''

while nombre != '0':
    nombre = input('Indica un nombre: ')
    if nombre != '0':
        caracteres += len(nombre)

print(caracteres)