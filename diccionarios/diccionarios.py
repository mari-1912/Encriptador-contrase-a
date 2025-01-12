#DICCIONARIOS

#vamos a hacer un diccionario como si fuera una pequeña biblioteca
biblio = {
    'Imperio':'Iria y Selene',
    'El Familiar':'Leigh Bardugo',
    'Hojas de dedalera':'Victoria Alvarez',
    'Placeres Mortales':'Belen Martinez'
    }

#vamos a pedirle al programa que nos diga cuál es el autor del libro Imperio
print(biblio['Imperio'])

'''Si ejecutamos un autor que no hayamos añadido nos va a aparecer una excepcion de tipo keyerror'''
#print(biblio['Sarah J Maas'])

'''para que nos indique un mensaje en estos casos en lugar de un error podemos usar la siguiente funcion'''
print(biblio.get('Trono de cristal','No está en la biblioteca')) 
'''con esto le estaríamos pidiendo que nos busque a la autora Sarah J Maas y que si no la encuentra,
nos muestre el mensaje por pantalla de que no esta en la biblioteca'''
print(biblio.get('Placeres Mortales'))

#queremos comprobar si el libro El Familiar y si el libro La novena casa están en la biblioteca
print('El Familiar' in biblio) #El Familiar si esta por lo que devuelve true
print('La novena casa' in biblio) #La novena casa no esta por lo que devuelve false

#Para imprimir por pantalla solamente las claves, es decir los titulos de los libros en este caso
print(biblio.keys())

#Para imprimir solamente los valores de dentro, en este caso solamente los autores
print(biblio.values())

#un metodo muy usado para que nos muestre toda la informacion del diccionario y que se suele usar dentro de
#los bucles for, es el metodo items
print(biblio.items())

#Para que nos diga cuantos libros hay en la biblioteca (es decir, cuantas claves hay)
print(len(biblio)) #nos sale que hay 4 libros

#Para eliminar todos los elementos de un diccionario
print(biblio.clear())