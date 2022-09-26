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
    num = int(input("Digite un numero por favor: "))
    divisors(num)


if __name__=="__main__":
    run()