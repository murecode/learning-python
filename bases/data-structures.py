

#---------------------'LISTAS'-------------------------------
# - Mutable - Ordenada - Duplicados - Heterogéneos - Iterable - Busqueda Eficiente O(1) -
list_1 = [7, "word", 52 ]
frutas = ["🍌", "🍇", "🍑"]
words = ["cama", "xilofono", "barco", "yuca", "avión", "zorro"] 

# Metodos
list_1.append("22") #<- agrega un elmnt al final de una list.
list_1.insert(2, "🐘") #<- insertar un elmnt en la list en un indice específicado. 
list_1.count("word") #<- cuenta el # de veces que un elemt especificado aparece en una list. 
list_1.extend(frutas) #<- agrega los elmnts de una list (u otro iterable) al final de otra list.
list_1.remove(52) #<- elimina la primera ocurrencia de un elemento específico en una list.
list_1.reverse() #<- inverte el orden de los elemts en una lista

# Output
print("LIST_1 =", list_1)

# Metodos
idx = list_1.index("🍌") #<- retorna la posición de la primera aparición de un elmnt especificado en una list. 
print("POSICION =", idx) 

word_sorted = words.sort(reverse=False, key=str) #<- ordenar los elemnts modificando la list original en orden ascendente o descendente.
print("WORDS ORDENADOS =", word_sorted)

delete_elem = list_1.pop(2) #<- elimina y retorna el elem en una posición específica de una lista.
print("ELEM DELTETED =", delete_elem)

clear_list = list_1.clear() #<- elimina todos los elementos de una lista
print("LIST_CLEAN =", clear_list) 




#---------------------'TUPLAS'-------------------------------
#TUPLAS -> Inmutable - Ordenada - Heterogéneos, Acceso eficiente
#útiles donde se requiere estabilidad y consistencia en los datos. 
my_tupla = (5,"tupla",True)


#---------------------'SET - CONJUNTO'-------------------------------
# - Mutable - Iterable - Únicos - Desordenado - Heterogéneo -
# la búsqueda eficiente debido a que internamente implementa Hash Table
set_1 = {9,7,True}
set_1.add('casa')
print("CONJUNTO =", set_1)

existe_elemento = 'cero' in set_1
print("¿EXISTE? =", existe_elemento)


#---------------------'DICCIONARIOS'-------------------------------
# - Pares clave-valor - Mutable - Claves Únicas - Desordenado - Iterable - Heterogéneo
# la búsqueda eficiente debido a que internamente implementa Hash Table

dict_1 = {
  'sara': [1.6, 'pasa'],
  'beto': {6, True},
  'sam': 'rico' 
}
print("KEYS =", dict_1.keys())
print("VALUES =", dict_1.values())

dict_3 = dict()
dict_3['carla'] = [1.6, 'pasa']
dict_3['beto'] = {6, True}
dict_3['sam'] = 'rico'
print("ITEMS =", dict_3.items())




#---------------------'ITERACIONES'-------------------------------

# ------ for loop ---------
for item_list in list_1:
  print("FOR LIST =", item_list)

for item_set in set_1:
  print("FOR SET =",item_set)

for item_dict in dict_3:
  print("FOR DICT =", item_dict) # itera claves


# ------ for loop con 'range()' ---------
count = 0
veces = range(6)

for _ in veces:
  count = count + 1
  print("LOOP # =", count)

print( list(veces) ) # casteamos 'veces' para ver su interior

# ------ for loop con 'enumerate' ---------
for idx, val in enumerate(list_1):
  print( idx, val )




