#empezamos creando una lista de cadenas de esta manera:
lista = ['lunes','martes','miercoles','jueves','viernes']
#para visualizar toda la lista:
print(lista)
#para visualizar simplemente un elemento que queramos de la lista según su índice:
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
#si queremos acceder según el índice pero a la inversa:
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
#indicarle los elementos que queremos con sublistas
#por ejemplo, si queremos llegar desde la posicion 0 a la 3:
print(lista[0:4])
print(lista[2:])
#y si lo queremos a la inversa, hay que añadir un paso negativo al final del slicing:
print(lista[-1:-4:-1])
print(lista[-2:-5:-1])

#Las listas también pueden tener otros tipos de valores
lista1 = ['lunes', 1, 'martes', 2, 'miercoles', 3, 'jueves', 4, 'viernes', 5, True]
print(lista1)
