#las lambda son funciones anonimas, es decir, funciones que no tienen nombre 
#y que se pueden usar en una sola linea de codigo   

#ejemplo 1
#definimos una funcion normal
def suma(a,b):
    return a+b

#definimos una funcion lambda
suma2 = lambda a,b: a+b #una sola linea de codigo

#ejemplo 2
#definimos una funcion normal
def par(x):
    if x%2 == 0:
        return True
    else:
        return False

#definimos una funcion lambda
par2 = lambda x: True if x%2 == 0 else False

#funcion lambda palindromo
palindromo = lambda string: string == string[::-1]
#print(palindromo("ana")) #true
#print(palindromo("hola")) #false
#print(palindromo("oso")) #true