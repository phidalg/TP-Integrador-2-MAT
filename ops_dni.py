

def obtener_digitos_unicos(dni):

    conjunto_digitos = []

    for digito in dni:

        if int(digito) not in conjunto_digitos:
            conjunto_digitos.append(int(digito))

    return conjunto_digitos



def ordenar_conjunto(conjunto):

    conjunto.sort()

    return conjunto



def calcular_union(conjunto1, conjunto2):

    union = conjunto1[:]

    for digito in conjunto2:

        if digito not in union:
            union.append(digito)

    return union



def calcular_interseccion(conjunto1, conjunto2):

    interseccion = []

    for digito in conjunto2:

        if digito in conjunto1:
            interseccion.append(digito)

    return interseccion



def calcular_diferencia(conjunto1, conjunto2):

    diferencia = []

    for digito in conjunto1:

        if digito not in conjunto2:
            diferencia.append(digito)

    return diferencia



def calcular_diferencia_simetrica(conjunto1, conjunto2):
    
    union = calcular_union(conjunto1, conjunto2)
    interseccion = calcular_interseccion(conjunto1, conjunto2)
    diferencia_simetrica = []

    for digito in union:
        if digito not in interseccion:
            diferencia_simetrica.append(digito)

    return diferencia_simetrica



def calcular_frecuencia_digitos(dni):

    frecuencia_digitos = []

    for char_digito in dni:
        digito = int(char_digito)

        encontrado = False
        for i in range(len(frecuencia_digitos)):
            if frecuencia_digitos[i][0] == digito:
                frecuencia_digitos[i][1] += 1
                encontrado = True
                break

        if not encontrado:
            frecuencia_digitos.append([digito, 1])

    frecuencia_digitos.sort()

    return frecuencia_digitos

def sumar_digitos_dni(dni):

    suma = 0

    for digito_str in dni:
        suma += int(digito_str)

    return suma



def verificar_diversidad_numerica(dni_str):

    conjunto_digitos_dni = obtener_digitos_unicos(dni_str)

    if len(conjunto_digitos_dni) < 5:
        return f"El DNI {dni_str} tiene diversidad numérica pequeña."
    else:
        return f"El DNI {dni_str} tiene diversidad numérica alta."



def verificar_comparten_digito_especifico(dni1_str, dni2_str, digito_a_buscar):

    conjunto_dni1 = obtener_digitos_unicos(dni1_str)
    conjunto_dni2 = obtener_digitos_unicos(dni2_str)

    if (digito_a_buscar in conjunto_dni1) and (digito_a_buscar in conjunto_dni2):
        return f"Los DNI {dni1_str} y {dni2_str} comparten el dígito {digito_a_buscar}."
    else:
        return f"Los DNI {dni1_str} y {dni2_str} no comparten el dígito {digito_a_buscar}."


def encontrar_digitos_comunes_alta_frecuencia(dni1_str, dni2_str, umbral_frecuencia=2):

    frecuencia_dni1 = calcular_frecuencia_digitos(dni1_str)
    frecuencia_dni2 = calcular_frecuencia_digitos(dni2_str)

    digitos_muy_comunes = []

    dict_frecuencia_dni1 = {digito: freq for digito, freq in frecuencia_dni1}
    dict_frecuencia_dni2 = {digito: freq for digito, freq in frecuencia_dni2}

    for digito_1, freq_1 in frecuencia_dni1:
        if freq_1 >= umbral_frecuencia:

            if digito_1 in dict_frecuencia_dni2 and dict_frecuencia_dni2[digito_1] >= umbral_frecuencia:
                digitos_muy_comunes.append(digito_1)
    
    digitos_muy_comunes.sort()
    return digitos_muy_comunes




#dni1 = input('Ingrese el primer DNI:')
#dni2 = input('Ingrese el segundo DNI:')

dni1 = '43397702'
dni2 = '37359451'
print("---")

# Obtener dígitos únicos
conjunto_dni1 = obtener_digitos_unicos(dni1)
conjunto_dni2 = obtener_digitos_unicos(dni2)

conjunto_dni1 = ordenar_conjunto(conjunto_dni1)
conjunto_dni2 = ordenar_conjunto(conjunto_dni2)

print(f'Dígitos únicos DNI 1: {conjunto_dni1}')
print(f'Dígitos únicos DNI 2: {conjunto_dni2}')
print("---")

# Unión
union = calcular_union(conjunto_dni1, conjunto_dni2)
print(f'Unión de DNI 1 y DNI 2: {union}')
print("---")

# Intersección
interseccion = calcular_interseccion(conjunto_dni1, conjunto_dni2)
print(f'Intersección de DNI 1 y DNI 2: {interseccion}')
print("---")

# Diferencia DNI1 - DNI2
dni1_menos_dni2 = calcular_diferencia(conjunto_dni1, conjunto_dni2)
print(f'Diferencia DNI 1 - DNI 2: {dni1_menos_dni2}')
print("---")

# Diferencia DNI2 - DNI1
dni2_menos_dni1 = calcular_diferencia(conjunto_dni2, conjunto_dni1)
print(f'Diferencia DNI 2 - DNI 1: {dni2_menos_dni1}')
print("---")

# Diferencia simétrica
diferencia_simetrica = calcular_diferencia_simetrica(conjunto_dni1, conjunto_dni2)
print(f'Diferencia simétrica: {diferencia_simetrica}')
print("---")

#Frecuencia DNI
frecuencia_dni1 = calcular_frecuencia_digitos(dni1)
print(f'Frecuencia de dígitos en DNI 1: {frecuencia_dni1}')
print("---")

frecuencia_dni2 = calcular_frecuencia_digitos(dni2)
print(f'Frecuencia de dígitos en DNI 2: {frecuencia_dni2}')
print("---")

#Suma de Digitos DNI
suma_dni1 = sumar_digitos_dni(dni1)
print(f'Suma de todos los dígitos del D.N.I. 1: {suma_dni1}')

suma_dni2 = sumar_digitos_dni(dni2)
print(f'Suma de todos los dígitos del D.N.I. 2: {suma_dni2}')
print("---")

# Verificamos la diversidad para cada DNI
print(verificar_diversidad_numerica(dni1))
print(verificar_diversidad_numerica(dni2))
print("---")

#Verificar si comparten el digito más alto
digito_buscado = 9
print(verificar_comparten_digito_especifico(dni1, dni2, digito_buscado))
print("---")

# Encontrar dígitos que se repiten 2 o más veces en ambos DNI
resultado = encontrar_digitos_comunes_alta_frecuencia(dni1, dni2, umbral_frecuencia=2)
print(f"Dígitos repetidos 2 o más veces en ambas listas: {resultado}")

