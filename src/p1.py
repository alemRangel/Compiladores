alfabeto = []
estados = []
estados_finales = []
trancision = {}
estado_inicial = []
caracteres_invalidos = {}
caminos = []


def funcion_recursiva(cadena, num_caracter, estado_actual, camino):
    if num_caracter < len(cadena):
        if cadena[num_caracter] in alfabeto:
            key = estado_actual + "," + cadena[num_caracter]
            posibles_estados = trancision[key].split(",")
            for posible_estado in posibles_estados:
                nuevo_camino = camino + "," + posible_estado
                funcion_recursiva(cadena, num_caracter+1, posible_estado, nuevo_camino)
        else:
            caracteres_invalidos[num_caracter] = cadena[num_caracter]
            funcion_recursiva(cadena, num_caracter + 1, estado_actual, camino)

    elif num_caracter == len(cadena):
        print("Para el camino " + camino + " la cadena es:")
        if estado_actual in estados_finales:
            print("Valida")
            for key in caracteres_invalidos:
                print("Con error en la posicion " + str(key+1) + " para el caracter" + caracteres_invalidos[key])
        else:
            print("Invalida")



def completar_automata():
    print("Complentando Automata")
    for estado in estados:
        for caracter in alfabeto:
            key = estado + "," + caracter
            if not(key in trancision):
                trancision[key] = "E"

        for caracter in alfabeto:
            key = "E" + "," + caracter
            trancision[key] = "E"

def leer_archivo():
    print("Leyendo archivo")
    archivo_automata = open("../archivosTexto/entradaP1.txt")
    for count, line in enumerate(archivo_automata):
        print(count)
        print(line)
        if count == 0:
            estados_raw = line.split(",")
            for estado in estados_raw:
                estados.append(estado.split("\n")[0])

        if count == 1:
            estados_finales_raw = line.split(",")
            for estado_final in estados_finales_raw:
                estados_finales.append(estado_final.split("\n")[0])

        if count == 2:
            estados_iniciales_raw = line.split(",")
            for estado_inicial_raw in estados_iniciales_raw:
                estado_inicial.append(estado_inicial_raw.split("\n")[0])

        if count == 3:
            alfabeto_raw = line.split(",")
            for caracter in alfabeto_raw:
                alfabeto.append(caracter.split("\n")[0])

        elif count > 3:
            trancision_raw = line.split(",")
            key = trancision_raw[0] + "," + trancision_raw[1]
            new_val = trancision_raw[2].split("\n")[0]
            if not(key in trancision):
                trancision[key] = new_val
            else:
                old_val = trancision[key]
                trancision[key] = old_val + "," + new_val

    archivo_automata.close()


if __name__ == "__main__":
    print("Hello There")
    leer_archivo()
    print("Estados:")
    print(estados)
    print("Estados finales")
    print(estados_finales)
    print("Estado inicial:")
    print(estado_inicial)
    print("Alfabeto:")
    print(alfabeto)
    print("Trancisiones")
    print(trancision)
    print("NFA Trancision")
    completar_automata()
    print("Trancision Completa")
    print(trancision)
    print("Inserte la cadena a verificar")
    cadena = input()
    funcion_recursiva(cadena, 0, estado_inicial[0], estado_inicial[0])
