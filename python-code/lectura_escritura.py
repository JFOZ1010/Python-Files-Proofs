#dentro de python podemos leer y escribir archivos
#para leer un archivo usamos la funcion open, con with que es para
#que el archivo se cierre automaticamente, y con el modo de lectura, 
#r, y el nombre del archivo, en este caso, archivo.txt

#la cosa es que la sentencia with nos ayuda a poder abrir el archivo
# y ayudar a que no se corrompa si el script que tenemos se cierra automaticamente, y   
# nos ayuda a que no se dañe el archivo.
def read():
    list_numbers = []
    with open('file.txt', 'r', encoding="utf-8") as f:
        #leemos el archivo y lo guardamos en una variable
        for line in f:
            list_numbers.append(int(line)) #convertimos a entero, porque line es un string
            list_numbers.sort() #ordenamos la lista
            #print(line)

        print(list_numbers)

#para escribir en un archivo usamos la funcion open de nuevo con with,
#pero esta vez con el modo de escritura, w, y el nombre del archivo
#en este caso, archivo.txt
def write():

    names = ['José', 'Facundo', 'Miguel', 'Pepe', 'Roberto', 'Rocío', 'Felipe']
    with open('names.txt', 'a', encoding="utf-8") as f:
        #escribimos en el archivo
        for name in names:
            f.write(name) #escribimos el nombre en el archivo
            f.write('\n') #un salto de linea es \n
            print(name)


def run():
    read()
    write()

if __name__ == '__main__':
    run()    