def main():
    my_list = [1, "hello", True, 4.5] #list
    my_dict = {"firstname": "Guido", "lastname": "Van Rossum"} #dict

# esta es una super lista de lista, que tiene diccionarios. 
    super_list = [
        {"firstname": "Guido", "lastname": "Van Rossum"},
        {"firstname": "Grace", "lastname": "Hopper"},
        {"firstname": "Alan", "lastname": "Turing"},
        {"firstname": "Linus", "lastname": "Torvalds"},
        {"firstname": "Larry", "lastname": "Page"},
    ]

#esta es una super lista de diccionarios, que tiene listas.
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for i in super_list:
        print(i)
        #print de espacio
    


#entry point -> inicializar o programa.
if __name__ == "__main__":
    main()

