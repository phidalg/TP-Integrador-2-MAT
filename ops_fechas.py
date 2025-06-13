def ingresar_datos(dato):
    lista = []
    contador = 0
    while True:
        contador += 1
        entrada = input(f"Ingrese {dato} del integrante {contador} del grupo, o ingrese x para terminar: ")
        if entrada.upper() == "X":
            return lista
        try:
            lista.append(int(entrada))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero o 'x' para salir.")
            contador -= 1  # No contar intentos fallidos

def contar_anios_pares(anios):
    pares, impares = 0, 0
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def grupo_z(anios): # Devuelve True si todos nacieron después del 2000
    for anio in anios:
        if anio < 2000:
            return False
    return True

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def hay_anio_bisiesto(anios): # Devuelve True si hay al menos un año bisiesto.
    for anio in anios:
        if es_bisiesto(anio):
            return True
    return False

def producto_cartesiano(conjunto1, conjunto2):
    producto = []
    for i in conjunto1:
        for j in conjunto2:
            producto.append((i, j))
    return producto


def operaciones_con_anios():
    print("\n*** Operaciones con años de nacimiento ***\n")
    anios = ingresar_datos("el año de nacimiento")
    print("Años ingresados: ", anios)
    pares, impares = contar_anios_pares(anios)
    print(f"{pares} años pares, {impares} años impares.")
    if grupo_z(anios):
        print("Grupo Z (Todos nacieron después del 2000).")
    if hay_anio_bisiesto(anios):
        print(f"Tenemos un año especial.")
    print("Para calcular el producto cartesiano entre los conjuntos Años y Edades, \nnecesitamos las edades de los integrantes del grupo.")
    edades = ingresar_datos("la edad")
    producto = producto_cartesiano(anios, edades)
    print(f"El produco cartesiano entre el conjunto Años y el conjunto Edades es {producto}.")

operaciones_con_anios()
