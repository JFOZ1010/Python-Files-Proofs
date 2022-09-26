def lista_numeros():

# The code is creating a list of numbers that are not divisible by 3 and then squaring them.

   lista_numeros = []

   for i in range(1,100):
        if(i%3 != 0):
            lista_numeros.append(i**2)

   print("lista de numeros al cuadrado: ", lista_numeros)




if __name__ == "__main__":
    lista_numeros()