#inicializar funcion
import numpy as np

def dictionary_comprehension():

    #dictionary comprehension ->
    my_dict = {i: i**3 for i in range(1,1000) if i%3 != 0}
    #print(my_dict)

    #dictionary comprehension se lee como: {i: i al cubo for i in rango de 1 a 100 si i no es divisible por 3}

    #reto

    my_dict_reto = {i: np.sqrt(i) for i in range(1,1000)}
    print(my_dict_reto)

#create entry point
if __name__ == "__main__":
    dictionary_comprehension()