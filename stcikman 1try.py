import random

 

def mostrar_menu():
    "mostrar el menu principal"
    print ("\n === menu de juegos ===")
    print("1. adivina el numero")
    print("2. ahorcado ")
    print("3. codigo secreto")
    print("4. revoltijo de palabra")
    print("salir")


# JUEGO 1: ADIVINA EL NUMERO

def jugar_adivina_numero ():
    """juego donde el usuario adivina un numero entre 100 y se le ba dando pistas"""
    numero_secreto = random.randint(1, 100)
    intentos = 6

    print("\nAdivina el numero...")
    
    for i in range (intentos):
        try:
            intento = int (input(f" intento {i+1}: "))
        except ValueError:
                print("error")
                continue
        
        if intento < numero_secreto: 
            print("el numero es mayor")
        elif intento > numero_secreto: 
            print("el numero es menor")
        else: 
            print(" ganaste")
            return

    print( f" perdiste. el numero era {numero_secreto}")


# JUEGO 2: AHORCADO

def jugar_ahorcado():
    ahorcado_visual = [
    """
     +---+
     |   |
         |
         |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========"""
]
    """el clasico ahorcado, intenta adivinar la palabra usando letra por letra, si la letra no esta incluida en la palabra perdera 1 intento"""

    palabras = ["python", "computadora", "gimnasio", "proteina", "deltoide", "programacion", "creatina", "definicion"]
    palabra = random.choice(palabras)
    progreso = ["_"] * len(palabra)
    intentos = 6
    

    print("\n juego del ahorcado")

    while intentos > 0:
        print("palabra:", "".join(progreso))
        letra =  input("ingresa una letra: ").lower()
        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    progreso[i] = letra
        else:
         intentos -= 1
        print(f"incorrecto, intentos restantes: {intentos}")
        print(ahorcado_visual[6 - intentos])

        if "_" not in progreso:
            print("\n¡FELICIDADES! 🎉🎉🎉")
            print("Ganaste, la palabra era:", palabra)
            print("""
            \o/
             |
            / \\
            """)
            return

    print("\n¡OH NO! 😢 Te quedaste sin intentos.")
    print(f"La palabra era: {palabra}")
    print("""
        +---+
         |   |
         O    |
        /|\\   |
        / \\   |
               |
         ========
    """)
    print("¡Mejor suerte la próxima vez! y vulve a intentarlo!!")


# JUEGO 3: CODIGO 

def jugar_codigo():
    "juego donde tendras que adivinar un codigo de 4 digitos usando combinaciones numericas, si algun numero de tu intento coincide con la respuesta correcta se guardaray te mostrara los que te faltan"
    codigo = [str(random.randint(0, 9)) for _ in range(4)]
    progreso = ["_"] * 4
    intentos = 7

   

    for i in range(intentos):
        intento = input (f"intento {i+1} - ingrese un codigo: ")
    
        if len(intento) != 4 or not intento.isdigit():
            print ("codigo invalido")
            continue

        for j in range (4):
            if intento [j] == codigo [j]:
                progreso [j] = intento[j]

        print ("progreso: ", " ".join(progreso))

        if progreso == codigo:
            print("ganaste")
            return
    print("perdiste. el codigo era: ", "".join(codigo))



#  JUEGO 4: REVOLTIJOOOO

def jugar_revoltijo():
    """juego donde el usuario debe adivinar una palabra revuelta"""

    palabras = ["codigo", "pesas","isquiotibiales", "pectoral"] 
    palabra_objetivo = random.choice(palabras)
    mezclada = list(palabra_objetivo)
    random.shuffle(mezclada)

    intentos = 3

    print("\nAdivina la palabra:", "".join(mezclada))
    

    for i in range (intentos):
        intento = input(f"Intento {i+1}: ").lower()

        if intento == palabra_objetivo:
            print ("correcto")
            return
        else:
            print("incorrecta")

    print("perdiste. palabra era: ", palabra_objetivo)



def main ():
    while True:
        mostrar_menu()
        opcion = input ( "seleccione una opcion: ")

        if opcion == "1":
            jugar_adivina_numero()
        elif opcion ==  "2":
            jugar_ahorcado()
        elif opcion == "3":
                jugar_codigo()
        elif opcion == "4":
            jugar_revoltijo()
        elif opcion == "5":
            print("saliendo del programa...")
            break
        else:
            print("opcion invalida")

if __name__ == "__main__":
    main ()

