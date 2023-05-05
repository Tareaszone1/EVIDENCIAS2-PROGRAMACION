# Pedir al usuario que ingrese 5 números por teclado y crear una lista con ellos
print("Ingrese 5 números por teclado:")
lista1 = [int(input()) for i in range(5)]

# Crear otra lista con los elementos de la primera lista multiplicados por 2
lista2 = [numero * 2 for numero in lista1]

# Mostrar en pantalla los elementos de la segunda lista
print("Los elementos de la segunda lista son:")
for numero in lista2:
    print(numero)