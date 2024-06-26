
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

#--------------------------'keyword argument'---------------------

# argumentos tipo 'keyword': los argumentos se pasan a la función utilizando...
# sus nombres correspondientes y son empaquetados en un diccionario dentro de la función.
def keyword_args(param1, param2, param3):
  print(f"No importa el orden {param1} {param2} {param3} de entrada")

keyword_args( param2="🍉", param1="🍌", param3="🍐" )


#----------------------'POSITIONAL ARGUMENTS | *args |  KEYWORD ARGUMENTS (**kwargs) ------------------------------
# los 'positional arguments' se pasan a la función en el orden en que...
# se definieron en su firma y se empaquetan internamente en una tupla.
def positional_args(param1, param2):
  print(param1, param2)

positional_args("Beto", "Murillo") # <- output: 'Beto Murillo'

# los *args, parámetro especial que se utiliza  para indicar que una función puede...
# recibir un número n de variables como argumentos posicionales. se logra colocando un asterisco (*) en un unico parametro 
# internamente almacena cada parametro en una tupla
def sumar_muchos(*params):
  return sum(params)

print( "*args = ", sumar_muchos(2,3,6) )  

# los **kwargs, indicar que la función puede recibir un número variable de argumentos de palabra clave (keyword arguments).
# internamente se implementa un diccionario
def simular_db(**kwparam):
  username = kwparam['user'] #<- acceder por clave, extrae dato y almacena en una variable

  print(f" Nombre: {username}")
  print("**kwargs = ", kwparam)

# Entrada: ejemplo con info de un base de datos 
simular_db(
  name_db ='mydatabase',
  url ='localhost/',
  user ='root',
  password ='1234',
  port ='3305',
  sin_valor = ""
  )


#-------------------------'PRACTICA *args y **kwargs' ---------------------------
# En este ejemplo se calcula y aplica un descuento y un impuesto a un numero 'n' de argumentos posicionales

# Entrada
product_prices_list = [52, 64, 70]
ajustes_dict = {
  'descuento' : 0.5,
  'impuesto'  : 0.9
}

# Operaciones
def calcular_precio_total(*params, **kwparams):
  precio_total = sum(params) # <- suma todos los elmts ingresados  
  descuento = kwparams.get('descuento', 0) # <- sino se indica un valor de descuento se asigna cero por defecto
  impuesto = kwparams.get('impuesto', 0) # <- sino se indica un valor de impuesto se asigna cero por defecto

  precio_total -= precio_total * descuento
  precio_total += (precio_total * impuesto)

  return precio_total

# Salida
final = calcular_precio_total(*product_prices_list, **ajustes_dict ) # <- (*) desempaqute la lista y (**) desempaqueta el diccionario 
print('Precio final = ', final) 


#-------------------------'ITERABLE UNPACKING' ---------------------------
# los elementos del iterable se desempaquetan y asignan a las...
# variables correspondientes. Esto se logra colocando un asterisco (*) en el argumento

# Input
iterable = (5, "tupla", True)

# Operaciones
def do_unpacking(*param):
  for elem in param:
    print(elem)

# Output
do_unpacking(iterable)  


#----------------------'DICTIONARY UNPACKING'------------------------------


#---------------------'ARGUMENTOS OPCIONALES'-------------------------------
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





