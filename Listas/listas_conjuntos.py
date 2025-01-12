#CONJUNTOS
  
#conjunto de elementos desordenados donde no pueden haber valores duplicados
conjunto = set()
conjunto = {1,2,3,'hello',True,1,2,3} #primero se debe crear con set() ya que si no python lo detecta como un diccionario
print(conjunto) #NO puede contener una lista dentro
#se ve que hay valores repetidos 1,2,3 en los conjuntos siempre son únicos así que aunque se dupliquen
#el sistema los va a detectar como valor único

#Para agregar mas elementos a un conjunto con add
conjunto.add(4) #no lo añade al final ni sigue un orden especifico
print(conjunto)

#Para eliminar un valor concreto del conjunto discard
conjunto.discard(True)

#Tambien se pueden buscar valores dentro del conjunto 
print(3 in conjunto)
print(5 not in conjunto)