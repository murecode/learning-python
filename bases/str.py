
sentence = "La cara de la {} muchacha es hermosa {}"
name_list = ["Beto", "Sara", "Camila"]
number = "4"

# find(), devuelve la posicion de la primera ocurrencia
print(sentence.find("h")) 

# split(), divide una cadena en varias subcadenas una lista de elmnts
print(sentence.split()) 

# rindex(), busca desde el final hacia el principio, retorna el idx donde comienza la ocurrencia
print(sentence.rindex('hermosa')) 

# count(), retorna el numero de veces que una subcadena aparece dentro de una cadena
print(sentence.count('cara'))

# index(), retorna la posición de la primera ocurrencia de una subcadena dentro de una cadena
print(sentence.index('es')) 

# join(), concatena elmnts de una lista en una sola cadena, usando otra cadena como separador.
print( "_".join(name_list) ) 

# isnumeric(), verifica y retorna True si el caracter es un numero
print(number.isnumeric()) 

# format(), permite la inserción de valores en posiciones específicas dentro de la cadena, el {} indica la posicion.
print(sentence.format(number, name_list))

# replace(), reemplazar todas las ocurrencias de una subcadena en una cadena dada con otra subcadena.
print(sentence.replace('La cara', 'El rostro'))