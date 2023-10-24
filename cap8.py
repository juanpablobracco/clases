#LISTAS
#num = [3, 4, 5, 7, 11, 123]
#for cada in num:
#    print(cada)

#print(sum(num))
#print(min(num))
#print(max(num))
#print(sum(num) / len(num))

#**Ejercicio 1: Escribe una función llamada recortar que toma una lista y la modifica, removiendo el primer y último elemento, y regresa None. Después escribe una
#función llamada medio que toma una lista y regresa una nueva lista que contiene
#todo excepto el primero y último elementos.

def recortar(lista):
    del lista[0]
    del lista[-1]
    print(lista)
    return None
def medio(lista):
    del lista[0]
    del lista[-1]
    return lista

#lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#recortar(lista)
#nueva_lista = medio(lista)
#print(nueva_lista)

#Ejercicio 2. revisar cual linea del siguiente codigo no se encuentra protegida

#Ejercicio 3. Reescribe el código guardián en el ejemplo de arriba sin las
#dos sentencias if. En vez de eso, utiliza una expresión lógica compuesta
#utilizando el operador lógico or con una sola sentencia if.
# manejador = open('mbox-short.txt')
# contador = 0
# for linea in manejador:
#     palabras = linea.split()
#     # print 'Depuración:', palabras
#     if len(palabras) == 0 or palabras[0] != 'From': continue# sentencia guardian que se encarga de preveer el fallo del programa en casod e encontrarse con una linea vacia de valores, probocando la busqueda del valor requerido sea un fallo,
#     try:
#         print(palabras[2])
#     except:
#         print("Line out of range:", palabras)
#         continue

# Ejercicio 4: Descargar una copia de un archivo www.py4e.com/code3/romeo.txt.
# Escribir un programa para abrir el archivo romeo.txt y leerlo línea
# por línea. Para cada línea, dividir la línea en una lista de palabras
# utilizando la función split. Para cada palabra, revisar si la palabra ya
# se encuentra previamente en la lista. Si la palabra no está en la lista,
# agregarla a la lista. Cuando el programa termine, ordenar e imprimir
# las palabras resultantes en orden alfabético.

# open_arc = open("romeo.txt")
# #read_arc = open_arc.read()
# lista_romeo = []
#
# for linea in open_arc:
#     linea = linea.rstrip() #quitamos el \n final
#     linea = linea.lower() #lo pasamos a minuscula
#     linea = linea.split() #creamos una lista de palabras
#     try:
#         for palabra in linea:
#             if palabra in lista_romeo: continue
#             else:
#                 lista_romeo.append(palabra)
#     except:
#         continue
# lista_romeo.sort()
# print(lista_romeo)

# Ejercicio 5: Escribir un programa para leer a través de datos de una bandeja de entrada de correo y cuando encuentres una línea que comience
# con “From”, dividir la línea en palabras utilizando la función split.
# Estamos interesados en quién envió el mensaje, lo cual es la segunda
# palabra en las líneas que comienzan con From.Tendrás que analizar la línea From e imprimir la segunda palabra de
# cada línea From, después tendrás que contar el número de líneas From
# (no incluir From:) e imprimir el total al final. Este es un buen ejemplo
# de salida con algunas líneas de salida removidas:

#archivo = input("Ingrese el nombre del archivo:\n")

# try:
#     man_a = open("mbox-short.txt")
# except:
#     print('No se puede abrir el archivo:', archivo)
#     exit()
# adress_list = []
# for linea in man_a:
#     linea = linea.rstrip()
#     if not linea.startswith("From"): continue
#     linea = linea.split()
#     adress_list.append(linea[1])
#
# print(adress_list)
# print("cantidad de adresses:", len(adress_list))
#
# Ejercicio 6: Reescribe el programa que pide al usuario una lista de
# números e imprime el máximo y el mínimo de los números al final cuando
# el usuario ingresa “hecho”. Escribe el programa para almacenar los
# números que el usuario ingrese en una lista, y utiliza las funciones max()
# y min() para calcular el máximo y el mínimo después de que el bucle
# termine

numb_list = []
while True:
    numb = input("Agregar siguiente numero a lista: ")
    try:
        numb = int(numb)
        numb_list.append(numb)
    except:
        if numb == "done": break
        print("ERROR \n Write done to finish.")
print(numb_list)
print("max numb:", max(numb_list))
print("min numb:", min(numb_list))
