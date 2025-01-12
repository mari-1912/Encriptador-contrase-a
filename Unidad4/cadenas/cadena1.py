#1. Escribir un programa que lea 5 nombres de la consola y calcule el total de caracteres.
caracteres = 0
for i in range(5):
    nombres = (input('Escribe un nombre'))
    caracteres += len(nombres)

print('El total de caracteres es: ', caracteres)