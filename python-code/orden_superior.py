from functools import reduce

# una funcion de orden superior es una funcion que 
# recibe como parametro una funcion. 

#ejemplo 1
def suma(a,b):
    return a+b

def operacion(funcion): #esta es una funcion de orden superior
    return funcion

#print(operacion(suma(2,3)))

# pero ahora dentro de las funciones de orden superior existen unas
# funciones que son muy conocidas en otros lenguajes de programacion
# como son map, filter y reduce.


# con FILTER
# filter es una funcion que recibe como parametro una funcion y una lista
# y devuelve una lista con los elementos que cumplen la condicion de la funcion

my_list = [1,2,3,4,5,6,7,8,9,10]
odd = list(filter(lambda x: x%2 != 0, my_list))
print(odd)

# con comprehension list. 
list_cuadrado = [i**2 for i in range(1,6)] #comprehension list. 
print("con comprehension", list_cuadrado)

#  con MAP
# map es una funcion que recibe como parametro una funcion y un iterable
# y devuelve un iterable con los resultados de aplicar la funcion a cada elemento
lista_2 = [1,2,3,4,5]
lista_potencia_2 = list(map(lambda x: x**2, lista_2))
print("con map: ", lista_potencia_2)

list_proof = [2,2,2,2,2]
one = 1
for i in list_proof:
    one = one * i
print("2^6: ", one)

# con REDUCE
# reduce es una funcion que recibe como parametro una funcion y un iterable
# y devuelve un valor que es el resultado de aplicar la funcion a cada elemento
# de forma sucesiva
lista_3 = [2,2,2,2,2]
lista_repetidos = reduce(lambda x,y: x*y, lista_3)
print("con reduce: ", lista_repetidos)



























