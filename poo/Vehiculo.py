class Vehiculo:
  fuel_level = 0
  speed = 0
  __model = "" # para simular privacidad en python se anteponen dos "barras al piso"

  # Esto vendria a ser un mtd constructor
  def __init__(self, distance_traveled, capacity):
    self.distance_traveled = distance_traveled
    self.capacity = capacity

  def arrancar(self):
    print("En marcha")


# Objetos
automovil = Vehiculo(120000, "4")
automovil.fuel_level = 80
automovil.arrancar()

motocicleta = Vehiculo(52000, "2")
motocicleta.fuel_level = 25
motocicleta.__model = "2015"

print("Model moto =", motocicleta.__model)
print("Fuel Lv.=", automovil.fuel_level)
print("Moto Vl. =", motocicleta.speed)


# Clase hija 
class Aereo(Vehiculo):
  pass

avionComercial = Aereo(12000, "150")
print(avionComercial.distance_traveled)

caza = Aereo(25000, "1")
print(caza.capacity)



#DOC
# pass, es una instrucción que no realiza ninguna operación...
# se utiliza como marcador de posición cuando la sintaxis ...
# requiere que haya una declaración, pero no se necesita realizar ninguna acción.

