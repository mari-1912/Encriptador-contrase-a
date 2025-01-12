'''1. Teniendo un array/List de números.
1. Sumar todos los números que contenga.
2. Eliminar repetidos.
3. Crear un arrray con sólo los números pares que contenga.
4. Determinar cuantos coincide la clave con el valor.
5. Devolver el array con los pares que contenga ordenados.
6. Determinar el índice del primer valor determiado. Ejemplo: El indice del
primer valor 10'''

mi_lista = [1,15,86,3,25,7,15,1]

#sumar los numeros
print(sum(mi_lista))

'''def sum(mi_lista):
    num_total = 0
    for numeros in mi_lista:
        total += numeros
    return total'''

#eliminar los repetidos
#IMPORTANTE NO SE PUEDE EJECUTAR UN FOR A LA VEZ QUE SE ELIMINAN ELEMENTOS DE UNA LISTA, SE PUEDE HACER CON UNA COPIA DE LA LISTA

'''def eliminar(mi_lista):
    repetidos = []
    copia_lista = mi_lista.copy()
    for i in range(len(mi_lista)):
        if copia_lista[i] in repetidos:
            del copia_lista[i]
    
        repetidos.append(copia_lista[i])
    
    return copia_lista

print(eliminar(mi_lista))'''

#eliminar los numeros repetidos
def eliminar(mi_lista):
    resultado = []
    
    for elemento in mi_lista:
        if elemento not in resultado:
            resultado.append(elemento)
    
    return resultado

mi_lista = [1, 15, 86, 3, 4, 25, 12, 7, 15, 1]
print(eliminar(mi_lista))


#crear una nueva lista con solo los numeros pares que contenga la lista principal

lista_pares = []

for num in mi_lista:
    if num%2==0:
        lista_pares.append(num)

print(lista_pares)

#devolver el array con los pares ordenados

lista_pares.sort()
print(lista_pares)

#determinar el indice del valor '25'
print(mi_lista.index(25))

#cuantos numeros coinciden la clave con el valor

print(mi_lista.items(4))
