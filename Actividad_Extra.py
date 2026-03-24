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

