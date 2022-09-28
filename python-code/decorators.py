def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs): #nested function def wrapper(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')    

        return result

    return funcion_c

@funcion_a
def suma(a, b):
    print(a + b)
    return a + b

def measure_time(function):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print(total, 'seconds' )
        return result

    return wrapper

@measure_time
def suma(a, b):
    import time
    time.sleep(1)
    return a + b

#print(suma(10, 20))

if __name__ == "__main__":
    decorador = funcion_a(suma)
    decorador(10, 20)