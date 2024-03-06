import random
import time

count = 0
def crea_vector(l):
    return [random.randint(0, 100000) for _ in range(l)]

def comprueba_orden(vec):
    print(str(vec))
    global count
    count += 1 
    print("Numero de Iteraciones:",count)
    for i in range(len(vec) - 1):
        if vec[i] > vec[i + 1]:
            return False
    return True

def bubble(l):
    tiempo_inicio = time.time()
    vector = crea_vector(l)
    while not comprueba_orden(vector):
        for i in range(len(vector) - 1):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]

    tiempo_fin = time.time()
    print("Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
    return vector


def aleatorio(longitud):
    tiempo_inicio = time.time()
    vector = crea_vector(longitud)
    while not comprueba_orden(vector):
        for i in range(len(vector)):
            random_index = random.randint(0, len(vector) - 1)
            vector[i], vector[random_index] = vector[random_index], vector[i]

    tiempo_fin = time.time()
    print("Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
    return vector
def insertion(l):
    tiempo_inicio = time.time()
    vector = crea_vector(l)
    while not comprueba_orden(vector):
        for i in range(1,len(vector)):
            valor = vector[i]
            j = i - 1
            while j >= 0 and valor < vector[j]:
                vector[j + 1] = vector[j]
                j -= 1
            vector[j + 1] = valor
    tiempo_fin = time.time()
    print("Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
    return vector
def Sort(l):
    tiempo_inicio = time.time()
    vector = crea_vector(l)
    while not comprueba_orden(vector):
        vector.sort()
    tiempo_fin = time.time()
    print("Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
    return vector
#def Shell(l):
    tiempo_inicio = time.time()
    vector = crea_vector(l)
    while not comprueba_orden(vector):
        for i in range(len(vector)):
            random_index = random.randint(0, len(vector) - 1)
            vector[i], vector[random_index] = vector[random_index], vector[i]#
            

    tiempo_fin = time.time()
    print("Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
    return vector
def mergeSort(l):
    tiempo_inicio = time.time()
    vector = crea_vector(l)
    

    tiempo_fin = time.time()
    print("Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
    return vector
def get_user_input():
    while True:
        metodo = input("Introduzca el método que desea utilizar para la ordenación\n 1: bubble\n 2: aleatorio\n 3: insercion\n 4: Método Sort de Python\n"
                    " 6: Merge\n q: para salir\n ")
        if metodo in ["1", "2", "3","4","5","6", "q"]:
            break
    global count 
    count = 0
    if metodo == "q":
        return metodo, None

    while True:
        longitud = input("Introduzca la longitud del vector a ordenar: ")
        if longitud.isdigit():
            return metodo, int(longitud)

switch_dict = {
    "1": bubble,
    "2": aleatorio,
    "3": insertion,
    "4": Sort,
    #"5": Shell
    #"6": merge
}

while True:
    metodo, longitud = get_user_input()
    if metodo == "q":
        break

    resultado = switch_dict.get(metodo)(longitud)
    print(resultado)