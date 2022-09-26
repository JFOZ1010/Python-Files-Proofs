#los tipos de excepciones en python son:
# 1. Excepciones de sintaxis
# 2. Excepciones de tiempo de ejecucion
# 3. Excepciones de logica
# los cuales son: try, except, else, finally

#la excepcion try es para probar un bloque de codigo
#la excepcion except es para manejar el error
#la excepcion else es para ejecutar un bloque de codigo si no hay errores
#la excepcion finally es para ejecutar un bloque de codigo, independientemente de si hay errores o no

#ejemplo de excepcion try except
def try_example():
    x = 5
    try:
        print(x)
    except:
        print("An exception occurred")

try_example()

#ejemplo de excepcion raise
def raise_example():
    x = -1
    try:
        if x < 0:
            raise Exception("Sorry, no numbers below zero")
    except Exception as e:
        print(e)

raise_example()

#ejemplo de finally
def finally_example():
    try:
        print("Hello")
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")
 
def divisors(number):
    divisors_for = []
    divisors_comprehension = []
    for i in range(1, number +1):
        if number % i == 0: #con un 1 no funciona, pero es de prueba
            divisors_for.append(i)
    print("numeros divisibles for: ", divisors_for)
    divisores = [divisors_comprehension.append(i) for i in range(1, number +1) if number % i == 0] #con 1 no funciona, pero es de prueba
    print("numeros divisibles List: ", divisors_comprehension)
    #verificar si dado un numero sus numeros hasta el son divisores con list comprehension  
    #divisores = [divisores.append(i) for i in range(1, number +1) if i % number == 0]



def run():
    try:
        num = int(input("Digite un numero por favor: "))
        divisors(num)
        if(num < 0):
            raise Exception("No se permiten numeros negativos")

    except Exception as e:
        print(e)

if __name__=="__main__":
    run()