#Actividades introductorias
#ACTIVIDAD 1: Escribe un programa que solicite al usuario su año de nacimiento y muestre en qué año cumplirá 18, 21 y 100 años.
anio_nacimiento= int(input("Ingresá tu año de nacimiento"))

print (f"Cumplirás 18 años en:{anio_nacimiento+18}")
print (f"Cumplirás 21 años en:{anio_nacimiento+21}")
print (f"Cumplirás 100 años en: {anio_nacimiento+100}")

#ACTIVIDAD 2: Escribe un programa que solicite al usuario una cantidad de segundos y muestre cuántas horas, minutos y segundos equivalen. 
# Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.

cantidad_segundos = int(input("Ingrese una cantidad de segundos"))
horas=(cantidad_segundos//3600)
minutos=(cantidad_segundos%3600)//60
segundos =(cantidad_segundos%60)
print(f"{cantidad_segundos} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")

#ACTIVIDAD 3: Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar del 1 al 10 utilizando un bucle for.

numero= int(input("Ingresá un número para ver su tabla:"))
print(f"Tabla de multiplicar del {numero}:")
for i in range (1,11):
    resultado= numero *i
    print (f"{numero} x {i} = {resultado}")

#ACTIVIDAD 4: Crea un programa que dado un número N ingresado por el usuario, imprima los números del 1 al N pero saltee los múltiplos de 5. 
# Nota: utilizá la sentencia continue donde haga falta.

n=int(input("Ingresá un numero N:"))

print (f'Números del 1 al {n} (sin múltiplos de 5):')
for numero in range (1,n+1):
    if numero % 5 == 0: 
        continue
    print (numero)

#ACTIVIDAD 5: Escribe un programa que simule una caja registradora: el usuario ingresa precios de productos de a uno. 
#Cuando ingresa 0, el programa se detiene y muestra el total acumulado. Nota: utilizá la sentencia break cuando haga falta.

total=0;
print ("Caja registradora (ingresá 0 para terminar):")
while True:
    precio= float(input("Ingresá el precio del producto:"))
    if precio==0:
        break
    total+=precio
print (f'Total a pagar: ${total:.2f}') #pasamos a decimales con {:.2f=2decimales}

#ACTIVIDAD 6: Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas: una con los múltiplos de 5 y otra con el resto de los números. 
# Imprimí ambas listas al finalizar.
n= int(input('Ingresá un número N:'))
multiplos_de_5=[] #lista vacía (array dinámico)
otros_numeros=[]
for numero in range (1, n+1):
    if numero % 5 == 0:
        multiplos_de_5.append(numero) #agregamos al final
    else:
        otros_numeros.append(numero)
print ('Múltiplos de 5:', multiplos_de_5)
print ('Otros números: ', otros_numeros)

#ACTIVIDAD 7: Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por espacios.
#Las palabras cortas deben ser excluidas del resultado final.

cantidad= int(input('¿Cuántas palabras vas a ingresar?'))
palabras=[]
for i in range (cantidad):
    palabra= input(f'Ingresá la palabra {i+1}:')
    palabras.append(palabra)
oracion=""
for palabra in palabras:
    if len(palabra) > 3:
        oracion+= palabra+""
print ('Oración resultante:', oracion.strip()) #strip()quita espacios extra al final