#crear funcion list_comprehension
def list_comprehension():
    #lists comprehension ->
    lista_numeros = [i**2 for i in range(1,100) if i%3 != 0]
    #print(lista_numeros)
#list comprehension se lee como: [i al cuadrado for i in rango de 1 a 100 si i no es divisible por 3]

    lista_reto = [i for i in range(1,100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(lista_reto)



if __name__ == "__main__":
    list_comprehension()