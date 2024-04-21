

# LIST -> Mutable - Ordenada - Elemnts repetidos - Heterogéneos - Iterable
my_list = [7, 'casa', False, '⚜️', '⚜️']
print("lista:", my_list)


#TUPLAS -> Inmutable - Ordenada - Heterogéneos
my_tupla = (5,"tupla",True)


# SET -> Mutable - Iterable - Elemts únicos - Desordenado - Heterogéneos
# la búsqueda eficiente debido a que internamente implementa Hash Table
my_set = {9,8,7,"cero",5,0}
my_set.add(True)
my_set.add('cero')
print("conjunto:", my_set)

existe_elemento = 'cero' in my_set
print("Existe en el Set:", existe_elemento)


# DICCIONARIO -> Pares clave-valor - Mutable - Claves unicas - Desordenado - Iterable - Claves únicas
# la búsqueda eficiente debido a que internamente implementa Hash Table
my_dict_1 = {
  'sara': [1.6, 'pasa'],
  'beto': {6, True},
  'sam': 'rico' 
}
print("dict_1:", my_dict_1.keys())

my_dict_2 = dict(
  carla = [1.6, 'pasa'],
  beto = {6, True},
  sam = 'rico' 
)
print("dict_2:", my_dict_2.values())

my_dict_3 = dict()
my_dict_3['carla'] = [1.6, 'pasa']
my_dict_3['beto'] = {6, True}
my_dict_3['sam'] = 'rico'
print("dict_3:", my_dict_3.items())


# ------ for loop ---------
for item_list in my_list:
  print(item_list)

for item_set in my_set:
  print(item_set)

for item_dict in my_dict_3:
  print(item_dict) # itera claves


# ------ for loop con 'range()' ---------
count = 0
veces = range(6)

for _ in veces:
  count = count + 1
  print("iteracion -> ", count)

print( list(veces) ) # casteamos 'veces' para ver su interior

# ------ for loop con 'enumerate' ---------
for idx, val in enumerate(my_list):
  print( idx, val )




