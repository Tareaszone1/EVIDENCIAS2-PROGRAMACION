# Pedir al usuario que ingrese una lista de números enteros separados por comas
print("Ingrese una lista de números enteros separados por comas:")
lista = input().split(",")

# Convertir cada elemento de la lista a un número entero
lista = [int(numero) for numero in lista]

# Crear dos variables para almacenar la suma de los elementos positivos y negativos
suma_positivos = 0
suma_negativos = 0

# Recorrer la lista y sumar los elementos según su signo
for numero in lista:
    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        suma_negativos += numero

# Mostrar en pantalla las sumas
print("La suma de los elementos positivos es:", suma_positivos)
print("La suma de los elementos negativos es:", suma_negativos)