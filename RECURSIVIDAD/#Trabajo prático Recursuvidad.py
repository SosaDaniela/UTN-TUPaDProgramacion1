#TRABAJO PRÁCTICO RECURSIVIDAD

#EJERCICIO 1
#Crea una función recursiva que calcule el factorial de un número. 
def factorial(x):
    f=1
    for i in range(1,x+1):
        f*= i
    return f

#Permitir que el usuario ingrese el numero
#el factorial debe ser de este mismo numero
num=int(input("Ingrese el numero del que desea saber el factorial: "))
resultado=factorial(num)
print(f"El factorial de {num} es {resultado}")

#EJERCICIO 2
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada
# Función recursiva para calcular Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

posicion = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")

#EJERCICIO 3
# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

#EJERCICIO 4
# Función recursiva para convertir decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))
if numero >= 0:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
else:
    print("Error: Debe ingresar un número entero positivo.")

#EJERCICIO 5
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 caracteres, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la subcadena sin los extremos
    return es_palindromo(palabra[1:-1])


texto = input("Ingrese una palabra (sin espacios ni tildes): ")
resultado = es_palindromo(texto)

if resultado:
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")

#EJERCICIO 6
def suma_digitos(n):
    # Caso base: si el número es menor a 10, ya es un solo dígito
    if n < 10:
        return n
    else:
        # Tomamos el último dígito con % y seguimos con el resto usando //
        return (n % 10) + suma_digitos(n // 10)


print(suma_digitos(1234))  
print(suma_digitos(9))     
print(suma_digitos(305))   

#EJERCICIO 7
# Función recursiva para contar bloques
def contar_bloques(n):
    # Caso base: si el nivel más bajo tiene 1 bloque, solo se necesita 1
    if n == 1:
        return 1
    else:
        # Caso recursivo: sumar los bloques del nivel actual + los de la pirámide de nivel (n-1)
        return n + contar_bloques(n - 1)

print(contar_bloques(1))  
print(contar_bloques(2))  
print(contar_bloques(4))  

#EJERCICIO 8
def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que revisar
    if numero == 0:
        return 0
    else:
        # Tomamos el último dígito con % 10
        ultimo = numero % 10
        # Si coincide con el dígito buscado, sumamos 1
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2)) 
print(contar_digito(5555, 5))     
print(contar_digito(123456, 7))    
