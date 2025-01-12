#conjuntos
a = {1,2,3}
b = {3,4,5}
#comprobamos si ambos son iguales
d = {1,2}
e = {2,1}
print(d==e) #en el caso de los conjuntos, da igual el orden, si tiene los mismos elementos son iguales!

#Operaciones que se pueden realizar sobre los conjuntos

#Para realizar una suma de conjuntos, se hace con '|'
c = a | b #se suman los valores a un mismo conjunto
print(c) 

#Para ver los elementos que se encuentran en ambos conjuntos '&'
f = a & b
print(f)

#Para ver la diferencia, es decir, los elementos de a que no están en b usamos '-'
g = a - b
print(g)

#Y la diferencia simetrica, que son los elementos que estan en a y los que estan en b pero no los comparten ambos
h = a ^ b
print(h)

#Creamos un nuevo conjunto
i  = {1,2,3,4,5}

#para ver si hay un subconjunto del conjunto
print(a.issubset(i)) #aqui estamos diciendo si a es un subconjunto de i y si lo es, porque los elementos de a
                    #se encuentran dentro de los elementos de i

'''sin embargo, tienen que coincidir todos los elementos del conjunto,
si al conjunto a le borramos por ejemplo el numero 2, ya nos daria False, porque no estan
todos los elementos y por lo tanto no es subconjunto de i
'''

'''tambien podemos comprobar si son disconexos, es decir, si el elemento a y el b
no comparten ninguno de sus elementos'''
print(a.isdisjoint(b))