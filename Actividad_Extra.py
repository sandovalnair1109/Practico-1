#Actividad Extra: Tabla de posiciones de torneo de futbol

#mostrar_menú
def mostrar_menu():
    print ('\n'+'='*40)
    print ('Torneo de fútbol - Tabla de posiciones')
    print('='*40)
    print ('1. Agregar equipo')
    print ('2. Registrar resultado')
    print ('3. Mostrar tabla')
    print ('4. Eliminar equipo')
    print ('5. Salir')
    print ('='*40)

#primera opción: agregar equipo (crear datos de equipo)
def agregar_equipo(tabla):
    nombre = input('Nombre del equipo:').strip().title()
    #validación
    if nombre in tabla:
        print(f'El equipo "{nombre}" ya existe')
        return
    #crear eqipo con estadísitcas en cero
    tabla[nombre]= {
        'puntos':0, 'partidos_jugados':0, 'partidos_ganados':0, 'partidos_empatados':0, 'partidos_perdidos':0, 'goles_a_favor':0,
        'goles_en_contra':0, 'diferencia_de_goles':0
    }
    print(f'Equipo "{nombre}" agregado')
#segunda opción: registrar resultado
def validar_marcador(marcador):
    """
    Validación: El marcador debe ser formato "4-2" o "0-0"
    Retorna: (goles_local, goles_visitante) o None si es inválido
    """
    try:
        partes = marcador.split('-')
        if len(partes) != 2:
            return None
        #convertir a enteros
        g_locales = int(partes[0].strip())
        g_visitantes = int(partes[1].strip())

        #validar que no sean negativos
        if g_locales < 0 or g_visitantes<0:
            return None
        return (g_locales,g_visitantes)
    except(ValueError,AttributeError):
        return None
    #tercera opción: mostrar tabla (registrar resultados visitante)
def registrar_resultado (tabla):
    if len(tabla) < 2:
        print('Necesitas al menos 2 equipos. ')
        return
    print("\nEquipos:", list (tabla.keys()))

    local = input('Equipo local: ').strip().title()
    visitante = input ('Equipo visitante: ').strip().title()
    marcador=input ('Marcador(formato 4-2):').strip()

    #ver si existen en la tabla
    if local not in tabla or visitante not in tabla:
        print ('Uno o ambos equipos no existen')
        return
    if local == visitante:
        print ('No ooueden ser el mismo equipo')
        return
    
    resultado= validar_marcador(marcador)

    if resultado is None:
        print ('Formato inválido. Usá 4-2, 0-0, etc.')
        return
    g_locales, g_visitantes = resultado
    # actualizar estadísticas del LOCAL
    tabla[local]["partidos_jugados"] += 1
    tabla[local]["goles_a_favor"] += g_locales
    tabla[local]["goles_en_contra"] += g_visitantes
    tabla[local]["diferencia_de_goles"] = tabla[local]["goles_a_favor"] - tabla[local]["goles_en_contra"]
    
    #actualizar estadísitcas del visitante
    tabla[visitante]['partidos_jugados'] += 1
    tabla[visitante]['goles_a_favor'] += g_visitantes
    tabla[visitante]['goles_en_contra'] += g_locales
    tabla[visitante]['diferencia_de_goles']+= tabla[visitante]['goles_a_favor'] -  tabla[visitante]['goles_en_contra']

    #calcular puntos según resultado
    if g_locales> g_visitantes:
        tabla[local]['partidos_ganados']+=1
        tabla[local]['puntos']+=3
        tabla[visitante]['partidos_perdidos']+=1
        print (f"{local} ganó {g_locales}-{g_visitantes}")

    elif g_locales<g_visitantes:
        tabla[visitante]['partidos_ganados']+=1
        tabla[visitante]['puntos']+=3
        tabla[local]['partidos_perdidos']+=1
        print (f'Empate {g_locales}-{g_visitantes}')
    else:
       tabla[local]['partidos_empatados'] += 1
       tabla[local]['puntos'] += 1
       tabla[visitante]['partidos_empatados'] += 1
       tabla[visitante]['puntos'] += 1
       print(f"Empate {g_locales}-{g_visitantes}")

