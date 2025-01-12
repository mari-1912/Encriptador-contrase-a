'''2. Teniendo un array/List de cadenas/strings.
1. Determinar sí hay cadenas repetidas.
2. Determinar cuantas vocales hay en todo el array.
3. Modificar el array eliminando las vocales de cada una de las cadenas
contenidas.
4. Crear un array resultado de unir todas las cadenas que contiene separadas
por un separador especificado (por ejemplo: ,).'''

mi_lista = ['hola', 'adios','hola','dia','noche','dia']

#ver si hay cadenas repetidas

copia_lista = []
repes = []
for word in mi_lista:
    if word not in copia_lista:
        copia_lista.append(word)
    elif word in copia_lista:
        repes.append(word)

print(repes)

#cuantas vocales hay en todo el array
def es_vocal(vocales):
    vocales = vocales.lower()
    return vocales=='a' or vocales=='e' or vocales=='i' or vocales=='o' or vocales=='u'

total_vocales = 0

for palabra in mi_lista:
    for letra in palabra:
        if es_vocal(letra):
            total_vocales+=1

print(total_vocales)

#modificar el array original eliminando las vocales

for i in range(len(mi_lista)):
    word = mi_lista[i]
    mi_lista[i] = "".join(letter for letter in word if not es_vocal(letter))

print(mi_lista)

#crea array con todas las cadenas unidas separadas por un elemento como ','

nueva_lista = ['hello', 'world','its','january']

union = ", ".join(nueva_lista)

print(union)