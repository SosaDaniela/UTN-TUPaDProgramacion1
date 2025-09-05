#EJERCICIO 1
EDAD = int (input("INGRESE SU EDAD: ") )
if EDAD > 18 :
    print ("ES MAYOR DE EDAD")
print ("FIN DE LA VERIFICACION DE EDAD")

#EJERCICIO 2
NOTA = int (input ("INGRESE SU NOTA"))
if NOTA >= 6 :
    print ("APROBADO")
else :
    print ("DESAPROBADO")

#EJERCICIO 3
NUMERO = int (input(" INGRESE UN NUMERO PAR"))
if NUMERO % 2 == 0 :
    print ("HA INGRESADO UN NUMERO PAR")
else:
    print ("POR FAVOR INGRESE UN NUMERO PAR")

#EJERCICIO 4
EDAD = int (input ("INGRESE SU EDAD : "))
if EDAD > 0  and EDAD < 12:
    print ("PERTENECE A LA CATEGORIA DE NIÑO/A")
elif EDAD >= 12  and EDAD < 18:
    print ("PERTENECE A LA CATEGORIA DE ADOLESCENTE")
elif EDAD >= 18  and EDAD < 30:
    print ("PERTENECE A LA CATEGORIA DE ADULTO/A JOVEN")
else :
    EDAD >= 30
    print ("PERTENECE A LA CATEGORIA DE ADULTO/A")


#EJERCICIO 5
CONT = int (input ("INGRESE UNA CONTRASEÑA QUE CONTENGA ENTRE 8 A 14 CARACTERES"))
if  len (CONT) >= 8 and len (CONT)<= 14 :
    print ("CONTRASEÑA CORRECTA")
else : 
    print ("POR FAVOR INGRESE UNA CONTRASEÑA CON LA CANTIDAD DE CARACTERES INDICADOS")


#EJERCICIO 6
import random 
import statistics
numeros_aleatorios = [random.randint (1 , 100) for i in range (10)]
from statistics import mode, median, mean
media =  mean (numeros_aleatorios)
moda =  mode (numeros_aleatorios)
mediana = median (numeros_aleatorios)
print( "Números: " , numeros_aleatorios)
print("La media es: ", mean )
print("La moda es: ",  mode)
print("La mediana es" , median )
if media > mediana and mediana > moda:
    print ("El sesgo es postivo")
elif media < mediana and mediana< moda :
    print ("El sesgo es negativo")
elif moda == mediana == media :
    print ("No hay sesgo")
else :
    print("La istribución no representa un sesgo claro (APROX. SIMETRICO)")


# EJERCICIO 7
palabras = input ("Ingrese una frase o palabra")
if palabras and palabras [-1].lower () in 'aeiou':
    print(f"EL USUARIO INGRESO: {palabras}!")
else : 
    print(f"EL USUARIO INGRESO: {palabras}")


#EJERCICIO 8 
NOMBR = input ("Ingrese su nommbre : ")
NUMB = int (input ("inGRESE UNO DE LOS SIGUIENTES NÚMEROS: 1, 2 Ó 3"))
if NUMB == 1:
    print(NOMBR.upper())
elif NUMB == 2 :
    print (NOMBR.lower())
elif NUMB == 3 :
    print(NOMBR.title())
else: 
 print ("NUMERO INVALIDO")


 #EJERCICIO 9
magn = float (input ("Ingrese la magnitud del Terremoto"))
if magn < 3:
    print ("Muy leve")
elif magn >= 3 and magn < 4:
    print ("Leve")
elif magn >= 4 and magn < 5:
    print ("Moderado")
elif magn >= 5 and magn < 6:
    print ("Fuerte")
elif magn >= 6 and magn < 7:
    print (" Muy Fuerte")
elif magn >= 7:
    print ("Extremo")
else: 
    print ("Ingrese un número válido")


#Ejercicio 10

HEMISFERIO = input("¿En qué hemisferio te encuentras? (N/S): ")
MES  = int(input("¿Qué mes es? (1-12): "))
DIA = int(input("¿Qué día es? (1-31): "))

#Determina y muestra la estación según el hemisferio , mes y fecha ingresada
if HEMISFERIO == "N":
    if (MES == 12 and DIA >= 21) or (MES in [1, 2]) or (MES == 3 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Invierno.")
    elif (MES == 3 and DIA >= 21) or (MES in [4, 5]) or (MES == 6 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Primavera.")
    elif (MES == 6 and DIA >= 21) or (MES in [7, 8]) or (MES == 9 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Verano.")
    elif (MES == 9 and DIA >= 21) or (MES in [10, 11]) or (MES == 12 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Otoño.")
    else:
        print("Fecha no válida.")
elif HEMISFERIO == "S":
    if (MES == 12 and DIA >= 21) or (MES in [1, 2]) or (MES == 3 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Verano.")
    elif (MES == 3 and DIA >= 21) or (MES in [4, 5]) or (MES == 6 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Otoño.")
    elif (MES == 6 and DIA >= 21) or (MES in [7, 8]) or (MES == 9 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Invierno.")
    elif (MES == 9 and DIA >= 21) or (MES in [10, 11]) or (MES == 12 and DIA <= 20):
        print("De acuerdo la fecha ingresada, estás en Primavera.")
    else:
        print("Fecha no válida.")
else:
    print("Hemisferio no válido.")