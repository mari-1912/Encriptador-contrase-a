#Ejercicio para concatenar cadenas
a = 'Hola como estas '
b = 'me llamo Pilar'
c = a + b
print(c)

#Acceso a caracteres de una cadena
cadena = 'Hola buenas noches'

print(cadena[5:11]) #hay que tener en cuenta que los espacios ocupan en el indice
'''con esta funcion nos imprimiria solamente la palabra buenas'''

#Para comprobar la longitud de una cadena
cadena1 = 'buenas noches estoy estudiando'
print(len(cadena1)) #nos muestra el número total de caracteres

#Transformar los caracteres de una cadena en MAYUSCULAS o en minusculas
mayus = 'MAYUSCULAS'
print(mayus.lower())
minus = 'minusculas'
print(minus.upper())

#5. Para eliminar los espacios en blanco del inicio y el final de una cadena usamos strip
espacios = '   Esta cadena tiene espacios   '
print(espacios) #en esta se pueden observar los espacios
print(espacios.strip()) #en esta ya no tiene espacios

#6. Replace para reemplazar una palabra o caracter en una cadena por otra
reemplazo = 'Hola buenas noches'
print(reemplazo) #en esta se lee el mensaje original hola buenas noches
print(reemplazo.replace('noches','tardes')) #se ha cambiado noches por tardes y se lee hola buenas tardes

#7. Dividir una cadena en una lista utilizando un separador split
separador = 'Esta, es, una, cadena, reemplazada, por, lista'
print(separador) #aqui se ve una cadena normal
print(separador.split(',')) #aqui se ve transformada en lista

#8. Para juntar una lista de palabras en una cadena se usa join
juntar = ['hola','buenas','noches']
print(juntar)
juntar_cadena = ' '.join(juntar) #aqui se ve como lista
print(juntar_cadena) #aqui ya se ve transformado en cadena

#9. Para ver si una subcadena está dentro de otra se usa in
aaa = 'Hola mundo'
bbb = 'mundo'
print('mundo' in bbb) #sale true porque la palabra mundo esta dentro de la cadena bbb
print('hola' in bbb) #sale false porque la palabra hola no esta en la cadena bbb sino en la cadena aaa

#10. Encontrar la posicion de la primera aparicion de una subcadena dentro de una cadena
ccc = 'Hola como estas'
print(ccc.find('como')) #nos da el valor 5, ya que el primer caracter de la palabra aparece en esa posicion en el indice
