#1. Crear una estructura de tipo Diccionaries que contenga las notas de (mates y lengua) de un alumno.

# creamos el diccionario
diccionario = {'mates':'5','lengua':'8'}
print(diccionario)

#para añadir una asignatura nueva al diccionario ya creado
diccionario['sistemas'] = '6'
print(diccionario)

#tambien se puede usar para modificar un valor ya dado usando su clave
diccionario['lengua'] = '7'
print(diccionario)

#para eliminar un solo valor del diccionario
del(diccionario['sistemas'])
print(diccionario)