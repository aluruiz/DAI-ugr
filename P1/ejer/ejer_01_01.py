import random

#Ejercicio 1
print("Juego de Adivinar")
numero = random.randrange(100)
print("Adivina el numero del 1 al 100")
adivina = int(input())
opciones = 10

while adivina != numero and opciones > 0:
    if adivina > numero:
        print("El numero buscado es menor. In3serta otro:")
        adivina = int(input())
    elif numero > adivina:
        print("El numero buscado es mayor. Inserta otro:")
        adivina = int(input())
    opciones-=1

if opciones == 0:
    print("Agotaste los intentos")
else:
    print("Enhorabuena acertaste!")
