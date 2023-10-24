#TUPLAS
# txt = 'Pero qué luz se deja ver allí a l'
# palabras = txt.split()
# t = list()
# print(t)
# for palabra in palabras:
#     t.append((len(palabra), palabra))
#     print("1", t)
# t.sort(reverse=True)# Ordena de mayor a menor las palabras
#
# res = list()
# for longitud, palabra in t:
#     res.append(palabra)#agrega a la lista "res" las palabras en orden previamente sorteados
#     #res.append(longitud)
# print("2", res)

# import string
# manejador = open("romeo.txt")
# # read_arc = manejador.read()
# # lista_romeo = []
# contadores = dict()
#
# for linea in manejador:
#     # linea = linea.rstrip() #quitamos el \n final
#     linea = linea.translate(str.maketrans("","", string.punctuation))
#     linea = linea.lower() #lo pasamos a minuscula
#     palabras = linea.split() #creamos una lista de palabras
#     try:
#         for palabra in palabras:
#             if palabra not in contadores:
#                 contadores[palabra] = 1
#             else:
#                 contadores[palabra] += 1
#             # if palabra in lista_romeo: continue
#             # else:
#             #     lista_romeo.append(palabra)
#     except:
#         print("error1")
#         continue
# #ordenamos el diccionario por valores
# lst = list()
# for clave, valor in list(contadores.items()):
#     # if len(clave) < 4: continue #si la clave(palabra) tiene un length menor a ... no agregarlo a la lista
#     lst.append((valor, clave))
#
# lst.sort(reverse=True)
#
# for clave, valor in lst[:10]:
#     print(clave, valor)
#
# # lista_romeo.sort()
# # print(lista_romeo)
# #
# # for apellido, nombre in directorio:
#     # print(nombre, apellido, directorio[apellido,nombre])
# # Este bucle recorre las claves en directorio, las cuales son tuplas. Asigna los
# # elementos de cada tupla a apellido y nombre, después imprime el nombre y el
# # número telefónico correspondiente
# #
# # sorted y reversed, que toman una secuencia como parámetro
# # y devuelven una secuencia nueva con los mismos elementos en un orden diferente.
#
# 10.11 Ejercicios
# Ejercicio 1: Revisa el programa anterior de este modo: Lee y analiza
# las líneas “From” y extrae las direcciones de correo. Cuenta el número
# de mensajes de cada persona utilizando un diccionario.
# Después de que todos los datos hayan sido leídos, imprime la persona con
# más envíos, creando una lista de tuplas (contador, email) del diccionario.
# Después ordena la lista en orden inverso e imprime la persona que tiene
# más envíos.
# Línea de ejemplo:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Ingresa un nombre de archivo: mbox-short.txt
# cwen@iupui.edu 5

# handler = open("mbox.txt")
# contador = dict()
#
# for line in handler:
#     if not line.startswith("From"): continue
#     line = line.split()
#     persona = line[1]
#     if persona not in contador:
#         contador[persona] = 1
#     else:
#         contador[persona] += 1
#
# # print("CONTADOR", contador)
#
# lst = list()
# for clave, valor in contador.items():
#     lst.append((valor, clave))
#
# # print("LST", lst)
#
# lst.sort(reverse=True)
#
# for clave,valor in lst[:1]:
#     print(valor, clave)

# Ejercicio 2: Este programa cuenta la distribución de la hora del día
# para cada uno de los mensajes. Puedes extraer la hora de la línea
# “From” buscando la cadena horaria y luego dividiendo la cadena en
# partes utilizando el carácter colon. Una vez que hayas acumulado las
# cuentas para cada hora, imprime las cuentas, una por línea, ordenadas
# por hora tal como se muestra debajo.

# handler = open("mbox.txt")
# contador = dict()
#
# for line in handler:
#     if not line.startswith("From"): continue
#     line = line.split()
#     if len(line) < 5: continue
#     hora = line[5]
#     hora = hora.split(":")
#     hora = hora[0]
#     if hora not in contador:
#         contador[hora] = 1
#     else:
#         contador[hora] += 1
#
# # print("CONTADOR", contador)
#
# lst = list()
# for clave, valor in contador.items():
#     lst.append((clave, valor))
#
# # print("LST", lst)
#
# lst.sort(reverse=False)
# print("Histograma de horas:")
# for clave,valor in lst[8:]:
# #     print(clave, valor)
#  Ejercicio 3: Escribe un programa que lee un archivo e imprime las
# letras en order decreciente de frecuencia. El programa debe convertir
# todas las entradas a minúsculas y contar solamente las letras a-z.
# El programa no debe contar espacios, dígitos, signos de puntuación,
# o cualquier cosa que no sean las letras a-z. Encuentra ejemplos de
# texto en idiomas diferentes, y observa cómo la frecuencia de letras es
# diferente en cada idioma. Compara tus resultados con las tablas en

import string
handler = open("arc.txt")
read = handler.read()
# lector = read(handler)
counts = dict()
#Purga de palabras, y contador de cantidad
for word in read:
    word = word.translate(word.maketrans('', '', string.punctuation))
    word = word.rstrip()
    word = word.lower()
    word = word.split()
    for letra in word:
        if letra not in counts:
            counts[letra] = 1
        else:
            counts[letra] += 1
# print("CONTADOR", counts)

lst = list()
for clave, valor in counts.items():
    lst.append((valor, clave))

lst.sort(reverse=True)

print("letters HISTOGRAM Español:")
for clave,valor in lst[:23]:
     print(clave, valor)
