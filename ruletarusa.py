import random

""" print("================================")
print("Bienvenido a la ruelta rusa")
print("================================")
comienzo = input("Escribe 'Y' si quieres disparar o 'N' si quieres terminar el juego : ")

while comienzo.lower() == "y":
    programa = random.randint(1,6)  # Programa genere un numero al azar entre 1 y 6.
    usuario = random.randint(1,6) # Se crea un numero random para usuario entre 1 y 6.
    if programa == usuario: #Comparar que numero de usuario sea igual a numero de programa.
        print("Moriste maquinola")
        break
    else:
        print("Estas a salvo por ahora")
    comienzo = input("Escribe 'Y' si quieres disparar o 'N' si quieres terminar el juego : ")
if comienzo.lower() == "n":
    print("saliendo del juego")
else:
    print("Juego Terminado") """


## Optimizarlo con While True y hacerlo funcion
def ruleta_rusa():
    print("================================")
    print("Bienvenido a la ruelta rusa")
    print("================================")

    while True:
        comienzo = input("Escribe 'Y' si quieres disparar o 'N' si quieres terminar el juego : ")

        if comienzo.lower() == "n":
            return "Saliendo del juego. Siempre supe que eras cagón"
        elif comienzo.lower() == "y":
            programa = random.randint(1,6)
            usuario = random.randint(1,6)
            if programa == usuario:
                return "Moriste maquinola"
            else:
                print("Estas a salvo por ahora.")
        else: 
            print("Entrada no valida. Por favor, ingresa 'Y' o 'N'.")

resultado = ruleta_rusa()

print(resultado)