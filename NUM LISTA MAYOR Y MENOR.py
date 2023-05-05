# Pedir al usuario que ingrese 10 números enteros separados por comas y crear una lista con ellos
print("Ingrese 10 números enteros separados por comas:")
lista = input().split(",")

# Convertir cada elemento de la lista a un número entero
lista = [int(numero) for numero in lista]

# Crear una lista vacía para guardar los números pares
pares = []

# Recorrer la lista y agregar los números pares a la lista de pares
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

# Mostrar en pantalla los resultados
print("De los 10 números ingresados:")
print("a. El valor del número máximo es:", max(lista))
print("b. El valor del número mínimo es:", min(lista))
print("c. Los números pares son:", pares)