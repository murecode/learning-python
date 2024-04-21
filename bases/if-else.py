edad = int( input("Ingresa edad: ") ) #se realiza un casteo de str a int
altura = int( input("Ingresa altura: ") )

if (edad >= 18 and altura >= 170) or (altura >= 165 and edad >= 25):
  print("puede participar")
else:
  print("No puede participar")

# --------- Operador ternario --------------