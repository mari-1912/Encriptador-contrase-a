#3. Escribir un programa que lea 5 nombres de la consola y calcule cuantas vocales se han introducido.

def es_vocal(letter):
    letter = letter.lower()
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

num_vocales = 0

for i in range(5):
    name = input('Nombre: ')
    for letter in name:
        if es_vocal(letter):
            num_vocales+= 1

print(num_vocales)