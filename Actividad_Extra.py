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

#cuarta opción: marcador
def mostrar_tabla(tabla):
    if not tabla:
        print ('No hay equipos en el torneo')
        return
    
    equipos_ordenados = sorted( 
        tabla.items(), 
        key=lambda item: (item[1]['puntos'], item[1]['diferencia_de_goles']),
        reverse=True
        )
    print ('\n' + '='*70)
    print(f"{'Pos':<4} {'Equipo':<15} {'Puntos':<4} {'Partidos Jugados':<3} {'Partidos Ganados':<3} {'Partidos Empatados':<3} {'Partios Perdidos':<3} {'Goles a Favor':<3} {'Goles en Contra':<3} {'Diferencia de Goles':<4}")

    print ('-'*70)

    #mostrar cada equipo
    for posicion, (nombre, stats) in enumerate (equipos_ordenados, start=1):
        print(f"{posicion:<4} {nombre:<15} "
              f"{stats['puntos']:<4} {stats['partidos_jugados']:<3} {stats['partidos_ganados']:<3} "
              f"{stats['partidos_empatados']:<3} {stats['partidos_perdidos']:<3} {stats['goles_a_favor']:<3} "
              f"{stats['goles_en_contra']:<3} {stats['diferencia_de_goles']:<4}")
    print('='*70)

#eliminación de un equipo
def eliminar_equipo(tabla):
    nombre= input('Equipo a eliminar: ').strip().title()
    if nombre not in tabla:
        print(f'El equipo "{nombre}" no existe')
        return
    confirmacion= input(f'¿Seguro que quieres eliminar a {nombre}? (s/n): ').lower()
    if confirmacion=='s':
        del tabla[nombre]
        print(f'Equipo "{nombre}" eliminado' )
    else:
        print('Cancelado')

#PROGRAMA PRINCIPAL
def main():
    tabla={} #diccionario vacío

    while True:
        mostrar_menu()
        opcion= input('\nElegí una opción(1-5): ').strip()
        
        if opcion == '1':
            agregar_equipo(tabla)
        elif opcion == '2':
            registrar_resultado(tabla)
        elif opcion== '3':
            mostrar_tabla(tabla)
        elif opcion== '4':
            eliminar_equipo(tabla)
        elif opcion == '5':
            print ('Saliendo del menú')
            break
        else:
            print ('Opcion inválida')

if __name__ == '__main__':
    main()

