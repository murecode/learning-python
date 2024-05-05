#---------------------'LAMBDA Fx Y Fx de orden superior'-------------------------------
# fx lambda o anomimas (sin nombre | pueden ser asignadas a variables | se pueden pasar como arg a fx de O.S )...
# ...se usan para realizar operaciones rapidas y pequeñas de forma expresiva.
# fx de O.S puede aceptar una o más funciones como argumentos. Puede devolver una función como resultado.

lambda e: e  # <- estructura basica de un lambda

# Datos de prueba
number_ls = [21, 80, 74, 12, 66, 125, 648]
student_ls = [('María', 3.7), ('José', 4.0), ('Pedro', 4.9), ('Santiago', 2.8)]
frutas_ls = ["manzana", "banano", "uva", "fresa", "mango"]

#Ej: fx-lmbd asignada a una varible
sumar = lambda a,b: a+b
print('suma lambda =', sumar(665, 582))

#Ej: sorted() ordenar la lista de > a < segun una llave en este caso las notas de los estudiantes
ordenar_calificaciones = sorted(student_ls, key=lambda n: n[1], reverse=True ) # <- la nota está ubicada en el indice [1] de la tupla
print('sorted() = ', ordenar_calificaciones)

#Ej: map() Agregar un sufujo a cada elem de la lista
sufijo = "/fruta"

frutas_sufijo = list( map( lambda s: s + sufijo, frutas_ls) ) # <- Se castea a una list para imprimir
print( 'map() =', frutas_sufijo )

#Ej: filter() filtrar elemts de una lista, dada una condicion. filtrar solo los pares de la list
pares_ls = list( filter(lambda n: n % 2 == 0, number_ls) ) # <- Se castea a una list para imprimir
print('filter() =', pares_ls)

#Ej: filter(), filtrar frutas, que empecen por la letra especificada
frutas_letra = list( filter( lambda s: s[0] == 'm' ,frutas_ls) )
print('filter() =', frutas_letra) 

# la fx reduce pertenece a un paquete externo de python
from functools import reduce

#Ej: reduce() aplica un operacion a cada elemt de una secuencia lo acumula reducuendolo a un solo valor.
#En este ejemplo 'acc' seria el acumulador y 'curr' el valor del elemento actual
reducir = reduce( lambda acc, curr: (acc + curr) * 2, number_ls)
print(reducir)

