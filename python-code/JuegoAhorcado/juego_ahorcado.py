import random
import os

#Author: @JFOZ1010
#Date: 2022-09-15

def juegoAhorcado():
    
    palabraRandom = []
    vidas = 5 #este es el numero de vidas que tiene el jugador

    #leemos el archivo de data.txt
    with open('./data.txt', 'r', encoding="utf-8") as f:
        #leemos el archivo y lo guardamos en una variable
        all_data = f.read()
        words = list(map(str, all_data.split())) #separamos las palabras por espacios y las guardamos en una lista, usando map
        word_random = random.choice(words) #seleccionamos una palabra al azar
        palabraRandom = list(word_random) #convertimos la palabra en una lista


        # creamos una lista comprehension para recorrer la lista de la palabra al azar, y reemplazar cada letra por un guion bajo.
        palabraGuiones = [palabra.replace(palabra, '_') for palabra in palabraRandom]
        print(palabraGuiones)

        # si la letra es correcta, se reemplaza el guion bajo por la letra
        for i in range(len(palabraRandom)):
            
            try:
                while palabraGuiones != palabraRandom:

                    #creamos un ASCII ART
                    print('''
                    Bienvenido al juego del ahorcado
                    Tienes 5 vidas, si fallas 5 veces, pierdes
                                    +---+
                                   |    |
                                   O    |
                                  /|\   |
                                  / \   |
                                        |
                     ====================''')
                    print("Life: ", vidas)
                    print("La palabra a adivinar tiene: ", len(palabraRandom), " letras")

                    letra = input('Ingresa una letra: ')
                    os.system('clear')        
                    if letra in palabraRandom:

                        palabraGuiones = [letra if letra == palabraRandom[i] else  palabraGuiones[i] for i in range(len(palabraRandom))] #esta lista comprehension, lo que hace es reemplazar el guion bajo por la letra que se ingreso.
                        print(palabraGuiones)
                    
                        if len(letra) > 1:
                            raise Exception('Debe ingresar una sola letra')
                        elif letra.isnumeric():
                            raise Exception('Debe ingresar una letra, no un número :D')
                    else:
                        print('La letra no está en la palabra')
                        vidas -= 1 #si la letra no es correcta, se resta una vida
                        if(vidas == 0):
                            print('Perdiste :(, ', 'La palabra era: ', word_random)
                            exit()                
            except Exception as e: #si la letra es un numero o un caracter especial, se lanza una excepcion
                print(e)
                continue

        if palabraRandom[i] == palabraGuiones[i]:
            palabraGuiones[i] = palabraRandom[i]
            print('Felicidades, ganaste! :D')

def run():

    juegoAhorcado()
    
if __name__ == '__main__':
    run()