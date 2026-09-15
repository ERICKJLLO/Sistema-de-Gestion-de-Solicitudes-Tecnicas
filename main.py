from sistema import Sistema
from solicitud import Solicitud


sistema = Sistema()

while True:

  print()
  print("SISTEMA DE GESTIÓN DE SOLICITUDES TÉCNICAS")
  print()
  print("1. Registrar solicitud")
  print("2. Ejecutar turno")
  print("3. Ejecutar automáticamente")
  print("4. Eliminar área")
  print("5. Agregar área")
  print("6. Consultar estado del sistema")
  print("7. Salir")
  print()

  opcion = input("Seleccione una opción: ")

  if opcion == "1":

    print()
    print("REGISTRAR SOLICITUD")

    id_solicitud = input("ID de la solicitud: ")
    descripcion = input("Descripción: ")
    prioridad = input("Prioridad (Alta/Normal): ")

    while prioridad != "Alta" and prioridad != "Normal":
      print("La prioridad debe ser Alta o Normal.")
      prioridad = input("Prioridad (Alta/Normal): ")

    solicitud = Solicitud(id_solicitud, descripcion, prioridad)

    sistema.registrar_solicitud(solicitud)

    print("Solicitud registrada correctamente.")

  elif opcion == "2":

    print()
    sistema.ejecutar_turno()

  elif opcion == "3":

    print()
    sistema.ejecutar_automaticamente()

  elif opcion == "4":

    print()
    print("ELIMINAR ÁREA")

    nombre = input("Nombre del área que desea eliminar: ")

    if sistema.eliminar_area(nombre):
      print("Área eliminada correctamente.")
    else:
      print("No se encontró el área o no se puede eliminar.")

  elif opcion == "5":

    print()
    print("AGREGAR ÁREA")

    nombre = input("Nombre de la nueva área: ")

    capacidad = input("Capacidad de la nueva área: ")

    while not capacidad.isdigit() or int(capacidad) < 1:
      print("La capacidad debe ser un número entero mayor que 0.")
      capacidad = input("Capacidad de la nueva área: ")

    capacidad = int(capacidad)

    sistema.agregar_area(nombre, capacidad)

  elif opcion == "6":

    sistema.mostrar_estado()

  elif opcion == "7":

    print("Programa finalizado.")
    break

  else:

    print("Opción no válida.")