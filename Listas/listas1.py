#Partimos teniendo esta lista de numeros:
numeros = [1,2,3,4,5]
print(numeros)

#Para determinar cuantos elementos tiene la lista:
print(len(numeros))

#queremos agregarle un elemento nuevo a la lista con el elemento append:
numeros.append(6) #en este caso el elemento se añade automaticamente al final de la lista
print(numeros)

# si queremos añadirle a un lugar concreto el elemento con insert:
numeros.insert(2,8) #lo que hemos indicado es que en el indice 2 queremos añadir el valor  8
print(numeros)

#si quieres añadir varios elementos a la vez al final de la lista se utiliza extend:
numeros.extend([7,8,9])
print(numeros)

#Podemos sumar dos listas para que se unan sus valores en una sola
lista1 = ['lunes','martes']
lista2 = ['miercoles','jueves','viernes']
lista3 = lista1 + lista2
print(lista3)

#Para saber si un elemento determinado está dentro de mi lista:
print('lunes' in lista3)
print(1 in numeros) #responde con True
print('sabado' in lista1) #responde con False

#Para saber exactamente en qué posición del índice se encuentra el elemento que queremos buscar con index:
print(numeros.index(5))
print(lista3.index('miercoles'))

#En la lista pueden haber valores repetidos, para saber cuantas veces se repite un valor count:
print(numeros.count(8))
print(lista3.count('lunes'))

#Para eliminar valores de la lista con pop
numeros.pop() #con esto elimina automaticamente el ultimo elemento de la lista, ya no estaria el 9
print(numeros)
#para eliminar un valor concreto, tenemos que indicarle su valor del indice donde se encuentra
numeros.pop(2)
print(numeros)

#si quieres eliminar el elemento pero no sabes en que indice esta ubicado con remove:
numeros.remove(8)
print(numeros)

#Por ultimo para eliminar todos los elementos de la lista se utiliza el metodo clear
numeros.clear()
print(numeros)

#le damos valores de nuevo
numeros = [1,2,3,4,5]
print(numeros)

#Para hacer que los elementos se vean al contrario, utilizamos reverse
numeros.reverse()
print(numeros)

#Si queremos que los elementos de la lista se dupliquen podemos hacerlo de la siguiente manera:
numeros = [1,2,3,4,5]*2
print(numeros)

#Tenemos esta otra lista con elementos desordenados
lista = [5,7,3,2,4,-2]

#queremos ordenarla en orden ascendente
lista.sort()
print(lista)

#si queremos ordenarla en orden invero con reverse
lista.sort(reverse=True)
print(lista)
