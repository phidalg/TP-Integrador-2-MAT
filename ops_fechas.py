def ingresarDatos(dato):
    lista = []
    contador = 0
    entrada = 0
    while True:
        contador += 1
        entrada = input(f"Ingrese el {dato} del integrante {contador} del grupo, o ingrese x para terminar: ")
        if entrada.upper() != "X":
            lista.append(entrada)
        else:
            return lista


def operacionesConAnios():
    print("*** Operaciones con años de nacimiento ***")
    years = ingresarDatos("año de nacimiento")
    print("Años ingresados: ", years)



