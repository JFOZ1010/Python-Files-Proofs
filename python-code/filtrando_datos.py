DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def filtrandoDatos():
    #all_javascript_devs = [worker["name"] for worker in DATA if worker["language"] == "javascript"] #List Comprehension
    #all_platzi_worker = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"] #List Comprehension

    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA)) #filter para todos los devs de python
    all_platzi_worker = list(map(lambda worker: worker["organization"] == "Platzi", all_python_devs)) #map para unificar con all_python_devs, y establecer true or false si trabajan en platzi

    adults = list(filter(lambda worker: worker["age"] > 18, DATA)) #funcion filter
    adults = list(map(lambda worker: worker["name"], adults)) #funcion map, mapeando solo por nombres de las personas mayores de edad.

    adults = [worker["name"] for worker in DATA if worker["age"] > 18] #List Comprehension, para obtener solo los nombres de las personas mayores de edad.
    #old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) #funcion map, mapeando por los nombres de las personas mayores de 70 años.
    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA] #list comprehension, para obtener los nombres de las personas mayores de 70 años.

    for workers in all_platzi_worker, adults, old_people:
        print(workers)
        

#entry point
if __name__ == '__main__':
    filtrandoDatos()