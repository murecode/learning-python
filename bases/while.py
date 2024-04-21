

exit_condition = "CONTINUAR"

while exit_condition == "CONTINUAR":
  nombre = input("Ingresa nombre: ")
  direccion = input("Ingresa direccion: ")

  print(f"Nombre: {nombre} - Direccion: {direccion}")

  exit_condition = input("¿Desea continuar?, Escriba CONTINUAR -> ")

  # Usar while cuando no sabemos cuantas veces se debe iterar