import random
import copy
#Diccionario de categorías (clave: nombre, valor: lista de palabras)
words_by_category ={'programacion': ['python','programa','variable','function','bucle','cadena','entero','lista'], 
    'animales':['perro','gato','elefante','jirafa','tigre','leon'], 
    'colores':['rojo','azul','verde','amarillo','violeta','naranja']
    }

#Mostrar categorías disponibles
print ('Categorias disponibles')
for category in words_by_category.keys():
    print (f'-{category}')

# Pedir entrada al usuario y normalizarla
chosen_category = input('Elegí una categoría: ').lower().strip()

# Quitar tildes si las hay
chosen_category = chosen_category.replace('ó', 'o').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ú', 'u')

# Validar que exista en el diccionario
while chosen_category not in words_by_category:
    print(f"'{chosen_category}' no es una categoría válida.")
    print("Opciones:", list(words_by_category.keys()))
    
    # Pedir de nuevo
    chosen_category = input('Elegí una categoría: ').lower().strip()
    chosen_category = chosen_category.replace('ó', 'o').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ú', 'u')

# Copiar palabras de la categoría elegida (para no modificar el original)
available_words = copy.copy(words_by_category[chosen_category])

print(f"\n{'='*50}")
print(f"¡COMENZAMOS! Categoría: {chosen_category.upper()}")
print(f"{'='*50}")

# WHILE EXTERIOR: Controla las rondas/múltiples partidas
while len(available_words) > 0:
    
    # Preparar nueva ronda (reiniciar todo)
    word = available_words.pop(random.randint(0, len(available_words) - 1))
    guessed = []
    attempts = 6
    score = 0
    
    print(f"\n{'='*50}")
    print(f"NUEVA RONDA")
    print(f"Palabra de {len(word)} letras")
    print(f"Palabras restantes en categoría: {len(available_words)}")
    print(f"{'='*50}\n")

    # WHILE INTERIOR: El juego de adivinar (tu código original)
    while attempts > 0:
        progress=""
        for letter in word:
            if letter in guessed:
                progress += letter +""
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print ('¡Ganaste!')
            score +=6       #Gana 6 puntos
            print (f'Tu puntaje final es: {score}')
            break
        print (f'Intentos restantes: {attempts}')
        print (f'Letras usadas: {', '.join(guessed)}')

        letter = input('Ingresá una letra: ')
        
        #Validación: debe ser exactamente UNA letra (a-z, A-Z)
        if len(letter) !=1 or not letter.isalpha():
            print ('Entrada no válida')
            continue

        if letter in guessed:
            print('Ya usaste esa letra')
        elif letter in word:
            guessed.append (letter)
            print ('¡Bien! Esa letra está en la palabra.') 
        else:
            guessed.append(letter)
            attempts-=1
            score-= 1 #pierde 1 punto
            print ('Esa letra no está en la palabra')
        print()
    else:
        score=0         #pierde, puntaje a 0
        print(f'¡Perdiste! La palabra era: {word}')
        print (f'Tu puntaje final: {score}')
    if len (available_words) > 0:
        play_again = input('\n¿Querés jugar otra vez? (s/n): ').lower().strip()
        if play_again != 's':
            print ('\n ¡Gracias por jugar!')
            break  # Sale del while exterior (termina todo el programa)
    else:
        print(f"\n{'='*50}")
        print(f"¡Jugaste todas las palabras de '{chosen_category}'!")
        print("No quedan más palabras.")
        print(f"{'='*50}")

print('\n¡Gracias por jugar!')