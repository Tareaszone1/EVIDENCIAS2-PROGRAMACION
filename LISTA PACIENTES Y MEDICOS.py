# Definir las listas de médicos y pacientes
medicos = []
pacientes = []

# Definir las funciones para registrar, mostrar y validar datos
def registrar_medico(lista):
  # Solicitar el ingreso de datos para el registro de un médico
  nombre = input("Ingrese el nombre del médico: ")
  especialidad = input("Ingrese la especialidad del médico: ")
  consultorio = input("Ingrese el consultorio del médico (una letra y un dígito): ")
  # Validar el dato del consultorio
  consultorio = validar_consultorio(consultorio)
  # Crear un diccionario con los datos del médico
  medico = {"nombre": nombre, "especialidad": especialidad, "consultorio": consultorio}
  # Agregar el diccionario a la lista de médicos
  lista.append(medico)

def registrar_paciente(lista):
  # Solicitar el ingreso de datos para el registro de un paciente
  nombre = input("Ingrese el nombre del paciente: ")
  edad = int(input("Ingrese la edad del paciente: "))
  fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (dd/mm/aaaa): ")
  # Validar el dato de la fecha de nacimiento
  fecha_nacimiento = validar_fecha(fecha_nacimiento)
  # Crear un diccionario con los datos del paciente
  paciente = {"nombre": nombre, "edad": edad, "fecha_nacimiento": fecha_nacimiento}
  # Agregar el diccionario a la lista de pacientes
  lista.append(paciente)

def mostrar_medicos(lista):
  # Mostrar en pantalla todos los datos de cada uno de los médicos registrados en la lista
  print("Lista de médicos registrados:")
  for medico in lista:
    print(f"Nombre: {medico['nombre']}")
    print(f"Especialidad: {medico['especialidad']}")
    print(f"Consultorio: {medico['consultorio']}")
    print()

def mostrar_pacientes(lista):
  # Mostrar en pantalla todos los datos de cada uno de los pacientes registrados en la lista
  print("Lista de pacientes registrados:")
  for paciente in lista:
    print(f"Nombre: {paciente['nombre']}")
    print(f"Edad: {paciente['edad']}")
    print(f"Fecha de nacimiento: {paciente['fecha_nacimiento']}")
    print()

def validar_fecha(fecha):
  # Verificar la validez del dato ingresado como fecha de nacimiento
  try:
    # Intentar convertir el dato a un objeto datetime
    from datetime import datetime
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    # Si no hay error, devolver el dato como una cadena
    return fecha.strftime("%d/%m/%Y")
  except ValueError:
    # Si hay error, solicitar el dato de nuevo
    print("Fecha inválida. Ingrese el dato nuevamente.")
    fecha = input("Ingrese la fecha de nacimiento del paciente (dd/mm/aaaa): ")
    return validar_fecha(fecha)

def validar_consultorio(consultorio):
  # Verificar que el dato ingresado como consultorio sea válido (una letra y un dígito)
  import re
  if re.match("^[A-Za-z][0-9]$", consultorio):
    # Si es válido, devolver el dato en mayúscula
    return consultorio.upper()
  else:
    # Si no es válido, solicitar el dato de nuevo
    print("Consultorio inválido. Ingrese el dato nuevamente.")
    consultorio = input("Ingrese el consultorio del médico (una letra y un dígito): ")
    return validar_consultorio(consultorio)

# Definir la función menú que muestra las opciones y llama a las funciones correspondientes
def menu():
  # Mostrar las opciones disponibles
  print("""
  Menú de opciones:
  [1] Registrar médico
  [2] Registrar paciente
  [3] Mostrar médicos
  [4] Mostrar pacientes
  [5] Salir
  """)
  
  # Solicitar al usuario que ingrese una opción
  opcion = input("Ingrese una opción: ")

  # Ejecutar la función correspondiente a la opción elegida
  if opcion == "1":
    registrar_medico(medicos)
    menu()
  
  elif opcion == "2":
    registrar_paciente(pacientes)
    menu()
  
  elif opcion == "3":
    mostrar_medicos(medicos)
    menu()
  
  elif opcion == "4":
    mostrar_pacientes(pacientes)
    menu()
  
  elif opcion == "5":
    print("Gracias por usar el programa. Adiós.")
  
  else:
    print("Opción inválida. Intente nuevamente.")
    menu()

# Llamar a la función menú para iniciar el programa
menu()