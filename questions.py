import random

words = [
    'python',
    'programa',
    'variable',
    'function',
    'bucle',
    'cadena',
    'entero',
    'lista'
]
word = random.choice(words)
guessed=[]
attempts=6

score=0

print ('Bienvenido al Ahorcado!')
print()
while attempts > 0:
    progress=""
    for letter in word:
        if letter in guessed:
            progress += letter +""
        else:
            progress += "_ "
    print(progress)
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
