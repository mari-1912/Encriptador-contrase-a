'''Crear una estructura de tipo Diccionaries que contenga las notas (de mates y
lengua) de una clase alumnos (varios alumnos)'''
alumnos = {
    'Pilar': {'mates':'5','lengua':'8'},
    'Pedro': {'mates':'6','lengua':'7'},
    'Lola': {'mates':'8','lengua':'8'}
}
print(alumnos)

#con esta estructura anterior de un diccionario dentro de otro, 
#1. borrar las notas de un alumno determinado

'''con esta manera de resolverlo, eliminamos toda la informacion incluyendo la clave 'Pedro'
del(alumnos['Pedro'])
print(alumnos)'''

#con esta otra solamente borramos la informacion de las notas, dejando el diccionario interno vacío

alumnos['Pedro'] = {}
print(alumnos)

#2. ahora queremos añadir un nuevo alumno
alumnos['Rocio'] = {'mates':'4','lengua':'5'}
print(alumnos)

#3. ahora queremos modificar las notas de un alumno
print(alumnos)
alumnos['Lola'] = {'mates':'7','lengua':'9'}
print(alumnos)

#4. para consultar las notas de un alumno
notas = alumnos['Pilar'].values()
print(notas)