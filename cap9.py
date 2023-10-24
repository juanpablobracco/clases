#Dictionaries
#similar to lists but asociete any kind of KEY whith a assigned value.

# eng2sp = dict()
# print(eng2sp)
#
# eng2sp["one"] = "uno"
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)
#
# val = eng2sp.values()
# if "uno" in val:
#     print("uno en valor")
# print(val)
#
# Escribe un programa que lee las palabras en words.txt y las almacena
# como claves en un diccionario. No importa qué valores tenga. Luego
# puedes utilizar el operador in como una forma rápida de revisar si una
# cadena está en el diccionario

# texto = open("words.txt")
# dict_txt = {}
# claves = 0
# for linea in texto:
#     linea = linea.rstrip()
#     linea = linea.split()
#     for palabra in linea:
#         claves = claves + 1
#         dict_txt[claves] = palabra
# print(dict_txt)

# palabra = 'brontosaurio'
# d = dict()
# for c in palabra:
#     d[c] = d.get(c,0) + 1
# print(d)


# import string #To clean the text and proccess only the words whitout any other character than letters.
#
# fname = input('Ingresa el nombre de archivo: ')
# try:
#     fhand = open(fname)
# except:
#     print('El archivo no se puede abrir:', fname)
#     exit()
# counts = dict()
# for line in fhand:
#     line = line.rstrip()
#     line = line.translate(line.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)
# for clave in counts:
#     print(clave, counts[clave])

# Ejercicio 2: Escribir un programa que clasifica cada mensaje de correo
# dependiendo del día de la semana en que se recibió. Para hacer esto
# busca las líneas que comienzan con “From”, después busca por la tercer
# palabra y mantén un contador para cada uno de los días de la semana.
# Al final del programa imprime los contenidos de tu diccionario (el orden
# no importa)

# archivo = input("Ingrese el nombre del archivo:\n")
#chatching the non found data
# try:
#     arc = open("mbox.txt")
# except:
#     print('No se puede abrir el archivo:', archivo)
#     exit()
#
# adress_list = dict()#creando un diccionario en la memoria para almacenar la informacion a procesar
#
# for linea in arc:
#     linea = linea.rstrip()#quitar los espacion finales
#     if not linea.startswith("From"): continue#solo procesar las lineas que comiencen con dicha palabra clave
#     list = linea.split()#crear una lista compuesta por las cadenas separadas por un espacio
#     if len(list) < 3: continue#chatching the error of those lines that have not la cantidad de valores necesarios para procesar
#     else:
#         word = list[2]#asigna a word el valor de la posicion 2 de la lista
#         if word not in adress_list:#funciones para generar un histograma entre claves unicas y cantidad de apariciones en el bucle
#                 adress_list[word] = 1
#         else:
#                 adress_list[word] += 1
#
# for clave in adress_list:#loop to print out the keys and assiged values in the adress_list dictionarie to been visualice one under the other
#     print(clave, adress_list[clave])

# Ejercicio 3: Escribe un programa para leer a través de un historial de
# correos, construye un histograma utilizando un diccionario para contar
# cuántos mensajes han llegado de cada dirección de correo electrónico, e
# imprime el diccionario

# try:
#     arc = open("mbox.txt")
# except:
#     print('No se puede abrir el archivo:', archivo)
#     exit()
#
# adress_list = dict()#creando un diccionario en la memoria para almacenar la informacion a procesar
#
# for linea in arc:
#     linea = linea.rstrip()#quitar los espacion finales
#     if not linea.startswith("From"): continue#solo procesar las lineas que comiencen con dicha palabra clave
#     list = linea.split()#crear una lista compuesta por las cadenas separadas por un espacio
#     if len(list) < 3: continue#chatching the error of those lines that have not la cantidad de valores necesarios para procesar
#     else:
#         word = list[1]#asigna a word el valor de la posicion 2 de la lista
#         if word not in adress_list:#funciones para generar un histograma entre claves unicas y cantidad de apariciones en el bucle
#                 adress_list[word] = 1
#         else:
#                 adress_list[word] += 1
# #busqueda de valor maximo de histograma en diccionario
# max_adress = None
# max_count = 0
# for val in adress_list:
#     get_max = adress_list.get(val, 0)
#     if get_max > max_count:
#         max_count = get_max
#         max_adress = val
#     else: continue
#
# print("\n", max_adress, max_count, "\n")
#
# for clave in adress_list:#loop to print out the keys and assiged values in the adress_list dictionarie to been visualice one under the other
#     print(clave, adress_list[clave])

# Ejercicio 4: Agrega código al programa anterior para determinar quién
# tiene la mayoría de mensajes en el archivo. Después de que todos los
# datos hayan sido leídos y el diccionario haya sido creado, mira a través
# del diccionario utilizando un bucle máximo (ve Capítulo 5: Bucles máximos y mínimos) para encontrar quién tiene la mayoría de mensajes e
# imprimir cuántos mensajes tiene esa persona.

# Ejercicio 5: Este programa almacena el nombre del dominio (en vez de
# la dirección) desde donde fue enviado el mensaje en vez de quién envió
# el mensaje (es decir, la dirección de correo electrónica completa). Al
# final del programa, imprime el contenido de tu diccionario.

try:
    arc = open("mbox.txt")
except:
    print('No se puede abrir el archivo:', archivo)
    exit()

adress_list = dict()#creando un diccionario en la memoria para almacenar la informacion a procesar

for linea in arc:
    linea = linea.rstrip()#quitar los espacion finales
    if not linea.startswith("From"): continue#solo procesar las lineas que comiencen con dicha palabra clave
    list = linea.split()#crear una lista compuesta por las cadenas separadas por un espacio
    if len(list) < 3: continue#chatching the error of those lines that have not la cantidad de valores necesarios para procesar
    else:
        dominio = list[1]#asigna a word el valor de la posicion 2 de la lista
        dominio = dominio.split("@")#volvemos a generar una lista pero separando la email adress.
        dominio = dominio[1]
        if dominio not in adress_list:#funciones para generar un histograma entre claves unicas y cantidad de apariciones en el bucle
                adress_list[dominio] = 1
        else:
                adress_list[dominio] += 1
#busqueda de valor maximo de histograma en diccionario
max_adress = None
max_count = 0
for val in adress_list:
    get_max = adress_list.get(val, 0)
    if get_max > max_count:
        max_count = get_max
        max_adress = val
    else: continue

print("\n", max_adress, max_count, "\n")

for k,v in adress_list.items():#loop to print out the keys and assiged values in the adress_list dictionarie to been visualice one under the other
    print(k,v) #ITEMS. retorna key y value de un diccioinario como tuplas
