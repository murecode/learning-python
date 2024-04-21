
def do_suma(param1, param2):
  """DOC: Esta función recibe dos numeros para sumarlos he imprime el resultado."""
  res = param1 + param2
  return res

resultado = do_suma(5, 3)
print( "SUMA =", resultado )


print( do_suma.__doc__ ) #1
#1. __doc__ , es un atributo especial, utiliza para acceder a la cadena de...
# documentación (docstring) asociada con un objeto proporcionar documentación...
# sobre su propósito, comportamiento, parámetros, valores de retorno, y etc.


#----------------------'positional arguments y *args'------------------------------

# los 'positional arguments' se pasan a la función en el orden en que...
# se definieron en su firma y se empaquetan internamente en una tupla.
def positional_args(param1, param2):
  print(param1, param2)

positional_args("Beto", "Murillo")


# los *args, parámetro especial que se utiliza  para indicar que una función puede...
# recibir un número n de variables como argumentos posicionales. se logra colocando un asterisco (*) en un unico parametro 
# internamente almacena cada parametro en una tupla
def sumar_muchos(*params):
  return sum(params)

print( "*args ->", sumar_muchos(2,3,6,4,5,8,4,2,2) )  


#--------------------------'keyword argument'---------------------

# argumentos tipo 'keyword': los argumentos se pasan a la función utilizando...
# sus nombres correspondientes y son empaquetados en un diccionario dentro de la función.
def keyword_args(param1, param2, param3):
  print(f"No importa el orden {param1} {param2} {param3} de entrada")

keyword_args( param2="🍉", param1="🍌", param3="🍐" )


#-------------------------'iterable unpacking' ---------------------------

iterable = (5, "tupla", True)
# los elementos del iterable se desempaquetan y asignan a las...
# variables correspondientes. Esto se logra colocando un asterisco (*) en el argumento
def do_unpacking(*param):
  for elem in param:
    print(elem)

do_unpacking(iterable)  


#----------------------'dictionay unpacking'------------------------------

# diccionario = {
#   'nombre': 'Carlos',
#   'apellido': 'Gomez',
#   'edad': 23
# }
#  permite asignar pares clave-valor de un diccionario a variables...
# individuales de manera compacta y eficiente. Esto se logra colocando dos asterisco (**) en el argumento

# def unpacking_dict(**param):
#   print()

# unpacking_dict(diccionario)


#---------------------'argumentos opcionales'-------------------------------

# tienen un valor predeterminado asignado en alguno de los parametros, si no...
# se especifican en la llamada la función utilizará automáticamente el valor predeterminado
def calcular_precio( producto, cantidad, precio_unitario, descuento=0 ): #<- ARGUMENTO OPCIONAL descuento en cero
  precio_final = (cantidad * precio_unitario) - descuento
  return producto, cantidad, precio_unitario, precio_final #<- 'Esto es 'MULTIPLE RETURN' para retornar múltiples valores se declara como una tupla sin parentesis

producto, cantidad, precio_unitario, precio_final = calcular_precio('manzana', 3, 2000) #<- esto es un 'unpacking' para desempaquetar la tupla de retorno
print('nombre: ', producto)
print('cantidad: ', cantidad)
print('precio unidad: ', precio_unitario)
print('precio final: ', precio_final)


