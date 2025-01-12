#7. Dado un texto quitar los números que contenga.

texto = 'hola buenas hoy es dia 11 del mes 1 de 2025'

for i in range(10):
    texto = texto.replace(str(i),'')


print(texto)