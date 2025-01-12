#TUPLAS
tupla = (1,'hello',[1,2,3],False)
print(tupla)
#En las tuplas a diferencia de en las listas, nunca se les puede modificar su contenido inicial
#lo unico que puede hacer con las tuplas es buscar los elementos
print(tupla[1])
print(tupla[2:])
print(1 in tupla)
print(tupla.index('hello'))
print(len(tupla))

#Tambien podemos convertir la tupla en una lista de la siguiente manera:
lista = list(tupla)
print(lista)