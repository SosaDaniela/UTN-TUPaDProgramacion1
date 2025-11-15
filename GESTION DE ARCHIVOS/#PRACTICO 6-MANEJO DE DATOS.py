#PRACTICO 6-MANEJO DE DATOS

#EJERICIO 1
#crear un diccionario con frutas 
precios_frutas={
    "Banana":1200,
    "Ananá":2500,
    "Melón":3000,
    "Uva":1450
}
#agregar tres frutas mas con su respectivo precio
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300


#EJERCICIO 2
#actualizar los precios..
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(f"El diccionario es: {precios_frutas}")

#EJERCICIO 3
#crear una lista solo con las frutas sin los precios
lista_frutas=["banana","ananá","melón","uva","naranja","manzana","pera"]
print(f"La lista de las frutas es: {lista_frutas}")

#EJERCICIO 4
#programa que permita almacenar y consultar nros telefonicos
#crear un diccionario vacio para luego agregarle los contactos que el usuario ingrese
contactos={}
#el  usuario tiene que cargar 5 contactos (nombres y numeros)
for r in range(5):
    nombre=input("Ingrese el nombre del contacto: ")
    numero_telefonico=int(input("Ingrese el numero del contacto: "))
    contactos[nombre]=numero_telefonico
#pedirle el nombre al usuario y mostrarle el numero correspondiente, si existe
verificacion_contacto=input("Ingrese un contacto para saber su número telefónico: ")
if verificacion_contacto in contactos:
    numero_telefonico=contactos[verificacion_contacto]
    print(f"El numero de telefono para {verificacion_contacto} es {numero_telefonico}")
else:
    print("El contacto no existe")

#EJERCICIO 5
#Solicita al usuario una frase e imprime:
frase=input("Ingrese una frase: ")
#usando .split(), separo las palabras de la frase del usuario
palabras=frase.split()

#Las palabras únicas (usando un set).
set_1=set(palabras)
print("Palabras únicas",set_1)

#Un diccionario con la cantidad de veces que aparece cada palabra.
#crear un dciiconario vacio para luego almacenar la cantidad de veces que se repita una palabra
cantidad={}
#crear una variable iteradora(palabra) que sera contada dentro de la variable palabras
for palabra in palabras:
    #si la palabra (iterador) se encuentra dentro del diccionario...
    if palabra in cantidad:
        #entonces a esa palabra se le suma uno
        cantidad[palabra]+=1
    else:
        #de lo contrario queda de la misma forma
        cantidad[palabra]=1
print("Conteo de palabras: ")
#imprime, recorriendo el diccionario, la clave y su valor
for palabra,cantidad in cantidad.items():
    print(f"{palabra}:{cantidad}")

#EJERCICIO 6
#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#al ingresar un bucle, permite pedirle 3 veces al usuario el nombre y las notas
for i in range(3):
    nombre = input("Nombre del alumno: ")
    #se guardan las notas en una tupla
    notas = (
        float(input("Nota 1: ")),
        float(input("Nota 2: ")),
        float(input("Nota 3: "))
    )
    #se saca el promedio sumando todas y se divide contando la cantidad de notas
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio}\n")

#EJERCICIO 7

#dados dos set de numeros, representando dos listas de estudiantes que aprobaron parcial 1 y 2
parcial_1={"Sanchez","Guzmán","Quiroga"}
parcial_2={"Sosa","Vivanco","Guzmán"}

#mostrar los que aprobaron ambos parciales
aprueban_ambos= parcial_1 & parcial_2
print(f"Aprobaron ambos parciales:{aprueban_ambos} ")

#mostrar los que aprueban uno de los dos
aprueban_uno= parcial_1 - parcial_2
aprueban_segundo=parcial_2-parcial_1
print(f"Aprueban solo uno de los dos: {aprueban_uno},{aprueban_segundo}")

#aprobaron al menos un parcial
aprueban_unodedos= parcial_1 | parcial_2
print(f"Aprueban al menos uno de dos: {aprueban_unodedos}")

#EJERCICIO 8

#armar un diccionario donde las claves sean productos y los valores el stock
productos={
    "fideos":3,
    "ravioles":2,
    "azúcar":4
}
#permitir al usuario
#consultar el stock de un producto
stock_producto=input("Ingrese el producto del que desea saber su stock: ").lower()
if stock_producto in productos:
    print(f"El stock de {stock_producto} es {productos[stock_producto]}")
#agregar unidades al stock si el producto ya existe
    cantidad_productos=int(input("Ingrese la cantidad de productos que quiere agregar al stock: "))
    productos[stock_producto]+=int(cantidad_productos)
    print(f"El nuevo stock de {stock_producto} es: {productos[stock_producto]}")
else:
    print("El producto no está en la lista.")
#EJERCICIO 9

#crear una agenda, las claves son tuplas de día y hora, y los valores son eventos
agenda={
    ("viernes","17:00"):"Evaluación de Programación",
    ("lunes","18:00"):"Evaluación de Matemática",
    ("martes","15:00"):"Evaluación de Organización Empresarial"
}
#permitir que el usuario consulte que actividad hay en cierto dia y horar
dia=input("Ingrese dia: ").lower()
horario=input("Ingrese el horario: ")

evento=agenda.get((dia,horario))
if evento:
    print(f"El evento para {dia} {horario} es: {evento}")
else:
    print("No hay eventos para ese día.")

#EJERCICIO 10

#crear un diccionario donde los paises sean las claves y las capitales los valores
paises={
    "Argentina":"Buenos Aires",
    "Brasil":"Rio de Janeiro",
    "Uruguay": "Montevideo"
}
print(f"El diccionario sin invertir es:{paises} ")
#invertir el diccionario
invertido={valor:clave for clave, valor in paises.items()}
print(f"La lista invertida es: {invertido}")