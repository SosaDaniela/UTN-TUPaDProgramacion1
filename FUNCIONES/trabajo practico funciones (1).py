#FUNCIONES
#EJERCICIO1
def imprimir_hola_mundo():
    return "Hola Mundo!"

saludo= imprimir_hola_mundo()
print(saludo)

#EJERCICIO2
def saludar_usuario(nombre):
    return (nombre)

nombre1=input("Ingresa tu nombre: ")
mostrar_nombre=saludar_usuario(nombre1)
print(f"Hola {mostrar_nombre}")

#EJERCICIO3
def informacion_personal(nombrecito,apellido,edad,residencia):
    return (f"Soy {nombrecito} {apellido}, tengo {edad} años y vivo en {residencia}")

name=input("Ingrese su nombre: ")
apell=input("Ingrese su apellido: ")
años=int(input("Ingrese su edad: "))
resi=input("Ingrese su lugar de residencia: ")

info=informacion_personal(name,apell,años,resi)
print(info)

#EJERCICIO4
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
# el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
# devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones 
# para mostrar los resultados.

def calcular_area_circulo(radio):
    import math
    return math.pi*radio**2

def calcular_perimetro_circulo(radioo):
    import math
    return 2*math.pi*radioo

radio1=float(input("Ingrese el radio del circulo: "))
area=calcular_area_circulo(radio1)
perimetro=calcular_perimetro_circulo(radio1)
print(f"El area del circulo es {area}, y el perimetro es {perimetro}")

#EJERCICIO5
#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(seg):
    return seg // 3600
segundos=int(input("ingrese la cantidad de segundos: "))
resultado=segundos_a_horas(segundos)
print(f"La cantidad de {segundos} segundos, dan un total de {resultado} horas")

#EJERCICIO6
#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_de_multilicar(numero):
    for i in range (11):
        print(f"{numero}*{i}={numero*i}")

num=int(input("Ingrese un numero para saber su tabla de multiplicacion: "))
resul=tabla_de_multilicar(num)

#EJERCICIO7
#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
#restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    print(f"La suma entre {a} y {b} es {a+b}")
    print(f"La resta entre {a} y {b} es {a-b}"),a*b,a/b
    print(f"La multiplicacion entre {a} y {b} es {a*b}")
    print(f"La division entre {a} y {b} es {a/b}")

resu=operaciones_basicas(1,2)

#EJERCICIO8
#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    imc=peso*(altura**2)
    return imc
pes=float(input("Ingrese su peso en kg: "))
alt=float(input("Ingrese su altura en m: "))
IMC=calcular_imc(pes,alt)
print(f"El indice de masa muscular de tu cuerpo es: {IMC}")

#EJERCICIO9
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celcius):
    f=9/5*celcius+32
    return f
grados_c=float(input("Ingrese la temperatura en grados C°: "))
far=celsius_a_fahrenheit(grados_c)
print(f"Los grados en celcius son {grados_c}°C, pasados a fahrenheit son {far}°F")

#EJERCICIO10
#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a,b,c):
    return (a+b+c)/3
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
promedio=calcular_promedio(num1,num2,num3)
print(f"El promedio entre los 3 numeros es de {promedio}")