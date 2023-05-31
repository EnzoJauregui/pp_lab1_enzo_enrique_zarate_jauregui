import json
import re

def leer_archivo(ruta: str) -> list:
    '''
    Recibe commo parametro una variable string 'ruta' que sera la ruta del archivo json que se quiere leer
    Abre el archivo json son un nombre y carga el contenido en una variable
    Retorna el contenido del archivo
    '''
    with open(ruta, 'r', encoding = 'utf-8') as archivo:
        contenido = json.load(archivo)

    return contenido['jugadores']

def join_lista(lista: list, flag_join: bool) -> str:
    '''
    Recibe una lista de strings y una variable booleana. 
    Si la lista tiene mas de 1 elemento, los separa por saltos de linea o ',' dependiendo de la variable booleana.
    Si la lista tiene un elemento, lo devuelve en string.
    Si la lista esta vacia, muestra un mensaje.
    Retorna una cadena de strings.
    '''
    if len(lista) > 1:
        if flag_join:
            cadena = '\n'.join(lista)
        else:
            cadena = ','.join(lista)
    elif len(lista) == 1:
        cadena = str(lista)
    else:
        print('LISTA VACIA')
        return -1
    return cadena

lista_jugadores = leer_archivo('C:\\Users\\enzo9\\OneDrive\\Documentos\\Programacion 1\\def\\dt.json')
#EJERCICIO 1 Y PARTE DEL EJERCICIO 5
def mostrar_jugadores_nombre_posicion(lista_jugadores: list, flag_jugador: bool) -> str:
    '''
    Recibe como parametros una lista de diccionarios que contiene la informacion de cada uno de los jugadores
    Muestra el nombre y la posicion de todos los jugadores.
    Retorna un string.
    '''
    lista_mensajes = []
    for jugador in lista_jugadores:
        if flag_jugador:
            lista_mensajes.append('{0} - {1}'.format(jugador['nombre'], jugador['posicion']))
        else:
            for clave, valor in jugador['estadisticas'].items():
                        if clave == 'promedio_puntos_por_partido':
                            lista_mensajes.append('{0}: {1} - {2}: {3}'.format('nombre'.upper(), jugador['nombre'], normalizar_dato(clave), valor))
    return join_lista(lista_mensajes, True)

def normalizar_dato(dato: str) -> str:
    '''
    Recibe una variable string como parametro y lo normaliza.
    retorna el dato normalizado.    
    '''
    dato_normalizado = dato.capitalize().replace('_', " ")
    return dato_normalizado

#EJERCICIO 2
def mostrar_estadisticas(lista_jugadores: list, indice_input: int) -> str:
    '''
    Recibe con parametros una lista de diccionarios que contiene la informacion de cada uno de los jugadores.
    Muestra el nombre, la posicion y las estadisticas del usuario ingresado por input.
    Retorna un string
    '''
    lista_mensajes = []
    lista_valores = []
    jugador = lista_jugadores[indice_input-1]

    for clave, valor in jugador['estadisticas'].items():
        lista_mensajes.append('{0}: {1}'.format(normalizar_dato(clave), valor))
        lista_valores.append(str(valor))
    
    print('\n----------{0}---------\n\nESTADISTICAS:\n{1}'.format(jugador['nombre'], join_lista(lista_mensajes, True)))

    contenido = '{0},{1},{2}'.format(jugador['nombre'], jugador['posicion'], join_lista(lista_valores, False))
    return contenido

#EJERCICIO 3
def guardar_csv(ruta: str,  contenido: str) -> bool:
    '''
    Recibe una variable string 'ruta' que sera la direccion donde se creara el archivo csv,
    y otra variable string 'contenido' que sera el contenido que se guardara en el archivo csv
    apre el archivo con el modo de escritura y carga el contenido a almacenar.
    si se crea o no el archivo, imprime un mensaje y declara un booleano asignandoles un valor
    retorna un booleano
    '''
    with open(ruta, 'w+') as archivo:
        byte = archivo.write(contenido)
    if byte > 0:
        print('Archivo CSV creado')
        flag_creado = True
    else:
        print('ERROR archivo csv no creado')
        flag_creado = False
    return flag_creado

#EJERCICIOS 4 Y 6 
def mostrar_si_pertenece_salon_fama(lista: list, flag_nombre: bool) -> None:
    """
    Esta función toma una lista de jugadores de baloncesto y una bandera booleana e imprime si cada
    jugador es miembro del Salón de la Fama del Baloncesto o imprime sus logros.
    
    :param lista: una lista de diccionarios que representan a jugadores de baloncesto, donde cada
    diccionario contiene información sobre un jugador, como su nombre y logros
    :type lista: list
    :param flag_nombre: Una bandera booleana que determina si mostrar el nombre del jugador junto con su
    estado como miembro del Salón de la Fama del Baloncesto o solo su lista de logros. Si flag_nombre es
    True, la función mostrará el nombre del jugador junto con su estado como miembro del Salón de la
    Fama. Si
    :type flag_nombre: bool
    """
    cadena = 'Miembro del Salon de la Fama del Baloncesto'

    for jugador in lista:
        if flag_nombre:
            if cadena in jugador['logros']:
                print('-{0} es {1}'.format(jugador['nombre'], cadena))
            else:
                print('-{0} no es {1}'.format(jugador['nombre'], cadena))
        else:
            print('----------{0}---------\n\nLOGROS:\n{1}'.format(jugador['nombre'], join_lista(jugador['logros'], True)))

def dividir(numerador: float, divisor: int) -> float:
    '''
    recibe una variable float y otra int
    verifica que el denominador sea distindo de 0
    retorna la division de las dos variables
    '''
    if divisor == 0:
        return 0
    else:
        return numerador / divisor           

def sumar_dato(lista_jugadores: list, dato: str) -> float:
    '''
    recibe una lista y un string como parametro
    acumula los valores dependiendo del dato ingresado
    retorna un float
    '''
    acumulador_dato = 0
    if len(lista_jugadores) > 0:
        for jugador in lista_jugadores:
            for clave, valor in jugador['estadisticas'].items():
                if clave == dato:
                    acumulador_dato += valor
    else: 
        print('ERROR LISTA')
    return acumulador_dato

#PARTE DE LOS EJERCICIOS 5 Y 16
def calcular_promedio_puntos_por_partido(lista: list, dato: str) -> float:
    '''
    Recibe una lista y un string como parametros
    Calcula el promedio llamando a las funciones dividir_dato y sumar_dato.
    Redondea con 2 decimales
    Retorna un float
    '''
    retorno = dividir(sumar_dato(lista, dato), len(lista))
    retorno_redondeado = round(retorno, 2)
    return retorno_redondeado

#PARTE DE LOS EJERCICIOS 5 Y 16
def cadena_promedio_total(dato, promedio, flag_promedio) -> str:
    """
    Esta función devuelve un mensaje de cadena que incluye el promedio de datos dados para todo el Dream
    Team o el promedio excluyendo al jugador con los puntos más bajos.
    
    :param dato: una cadena que representa el tipo de datos que se procesan (por ejemplo, "promedio de
    puntos")
    :param promedio: El valor promedio de un cierto punto de datos (por ejemplo, puntos anotados,
    rebotes, asistencias) para un equipo o subconjunto del equipo
    :param flag_promedio: Una bandera booleana que indica si el valor promedio es el promedio de todo el
    Dream Team o el promedio excluyendo al jugador con los puntos más bajos
    :return: un mensaje de cadena que incluye el promedio de un dato dado para todo el Dream Team o el
    promedio excluyendo al jugador con los puntos más bajos, según el valor del parámetro flag_promedio.
    El mensaje también incluye los datos normalizados (mediante la función normalizar_dato) y el valor
    correspondiente de la media.
    """
    if flag_promedio:
        mensaje = '\n{0} de todo el equipo del Dream Team es: {1}\n'.format(normalizar_dato(dato), promedio)
    else:
        mensaje = 'El {0} del equipo excluyendo al jugador que menos puntos tiene: {1}'.format(normalizar_dato(dato), promedio)

    return mensaje

#PARTE DE LOS EJERCICIOS 5 Y 20
def ordenar_palabras(lista_jugadores: list, key_string: str, flag: bool) -> list:
    """
    Esta función ordena una lista de diccionarios por una cadena de clave específica en orden ascendente
    o descendente.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus datos
    :type lista_jugadores: list
    :param key_string: El parámetro key_string es una cadena que representa la clave cuyo valor es un string
    :type key_string: str
    :param flag: El parámetro flag es un valor booleano que determina el orden de clasificación. Si flag
    es True, la función ordenará la lista en orden ascendente. Si la bandera es Falsa, la función
    ordenará la lista en orden descendente
    :type flag: bool
    :return: una lista ordenada de jugadores basada en los parámetros key_string y flag.
    """
    rango = len(lista_jugadores)
    flag_swap = True
    while flag_swap:
        flag_swap = False
        rango -= 1
        for i in range(rango):
            if flag == False and lista_jugadores[i][key_string] > lista_jugadores[i+1][key_string] or\
                flag == True and lista_jugadores[i][key_string] < lista_jugadores[i+1][key_string]:
                lista_jugadores[i], lista_jugadores[i+1] = lista_jugadores[i+1], lista_jugadores[i]
                flag_swap = True

    return lista_jugadores

#PARTE DE EJERCICIOS 7, 8, 9, 13, 14 Y 19
def calcular_jugador_mayor_estadistica_dato(lista_jugadores: list, dato: str) -> list:
    '''
    Recibe como parametros una lista de diccionarios que contiene la informacion de cada uno de los jugadores
    y una variable string 'dato' que seran una de las keys del diccionario de'estadisticas, y calcula cual es el mayor valor
    retorna un strig
    '''
    lista_jugador_max = []
    if len(lista_jugadores) != 0:
        for i in range(len(lista_jugadores)):
            estadisticas = lista_jugadores[i]['estadisticas']

            for clave in estadisticas:
                if clave == dato:
                    if i == 0 or max_valor_dato < estadisticas[dato]:
                        max_valor_dato = lista_jugadores[0]['estadisticas'][dato]
                        max_valor_dato = estadisticas[dato]
                        lista_jugador_max = [lista_jugadores[i]]

                    elif max_valor_dato == estadisticas[dato]:
                        lista_jugador_max.append(lista_jugadores[i])
        
        return lista_jugador_max
    else: 
        print('LISTA VACIA')

#PARTE DE EJERCICIOS 7, 8, 9, 13, 14 Y 19
def mostrar_jugador_estadistica_dato(lista: list, dato: str) -> None:
    '''
    Recibe como parametros una lista de diccionarios que contiene la informacion de los jugadores y una variable string que representa una
    key del diccionario 'estadisticas'
    Imprime una cadena formateada
    return: None
    '''
    print('\nCoincidencias encontradas: {0}\n'.format(len(lista)))

    for jugador in lista:
            print('Nombre: {0} - {1}: {2}'.format(jugador['nombre'], normalizar_dato(dato), jugador['estadisticas'][dato]))

#EJERCICION 10, 11, 12, 15, 18 Y PARTE DEL 20
def mayor_cantidad_dato(lista_jugadores: list, dato: str, numero: int) -> str:
    """
    La función toma una lista de jugadores y una estadística específica y devuelve los nombres y valores
    de los jugadores que tienen un valor más alto para esa estadística que un número dado.
    
    :param lista_jugadores: Una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre, posición y estadísticas
    :type lista_jugadores: list
    :param dato: una cadena que representa la estadística a comparar (por ejemplo, "puntos", "rebotes",
    "asistencias")
    :type dato: str
    :param numero: El valor que deben superar los datos de los jugadores para que se incluyan en la
    salida
    :type numero: int
    :return: ya sea una cadena con los nombres y estadísticas de los jugadores que tienen un valor mayor
    que el número dado para el tipo de datos dado, o una cadena que indica que ningún jugador tiene un
    valor mayor que el número dado para el tipo de datos dado.
    """
    
    lista_cadenas = []
    flag_ingreso = False

    for jugador in lista_jugadores:
        for clave, valor in jugador['estadisticas'].items():
            if clave == dato:
                if valor > numero:
                    flag_ingreso = True

                    if dato == 'porcentaje_tiros_de_campo':
                        lista_cadenas.append('NOMBRE: {0} - POSICION: {1} - {2}: {3}'.format(jugador['nombre'], jugador['posicion'], normalizar_dato(dato), valor))
                    else:
                        lista_cadenas.append('NOMBRE: {0} - {1}: {2}'.format(jugador['nombre'], normalizar_dato(dato), valor))

    if flag_ingreso: 
        return join_lista(lista_cadenas, True)
    else:
        return 'Ninguno supera este valor'

#PARTE DEL EJERCICIO 16
def ordenar_estadistica_dato_descendente(lista_jugadores: list, dato) -> list:
    """
    Esta función ordena una lista de jugadores en orden descendente según una estadística dada.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    sus estadísticas
    :type lista_jugadores: list
    :param dato: El parámetro "dato" es una clave que representa la estadística específica que se
    utilizará para ordenar la lista de jugadores en orden descendente. Se supone que cada jugador de la
    lista tiene un diccionario de estadísticas, y la tecla "dato" se utiliza para acceder al valor de la
    estadística específica de cada jugador
    :return: una lista de jugadores ordenados en orden descendente en función de una estadística
    determinada.
    """
    rango = len(lista_jugadores)
    flag_swap = True
    while flag_swap:
        flag_swap = False
        rango -= 1
        for i in range(rango):
            if lista_jugadores[i]['estadisticas'][dato] < lista_jugadores[i+1]['estadisticas'][dato]:
                lista_jugadores[i], lista_jugadores[i+1] = lista_jugadores[i+1], lista_jugadores[i]
                flag_swap = True
    
    return lista_jugadores

# EJERCICIO 17
def jugador_con_mas_logros(lista_jugadores: list) -> list:
    """
    Esta función toma una lista de jugadores y devuelve el jugador con más logros y su lista de logros.
    :param lista_jugadores: El parámetro de entrada es una lista de diccionarios que representan a los
    jugadores, donde cada diccionario contiene información sobre el nombre y los logros de un jugador
    :type lista_jugadores: list
    :return: una cadena que incluye el nombre del jugador con más logros y una lista de sus logros.
    """
    rango = len(lista_jugadores)

    for indice in range(rango):
        if indice == 0 or len(lista_jugadores[indice]['logros']) > max_logros:
            max_logros = len(lista_jugadores[indice]['logros'])
            indice_max = indice
    
    cadena = '\n----------{0}---------\n\nLOGROS:\n{1}'.format(lista_jugadores[indice_max]['nombre'], join_lista(lista_jugadores[indice_max]['logros'], True))
    return cadena

#EJERCICIO 21(BONUS)
def agregar_posicion_ranking_dato(lista_jugadores: list) -> str:
    """
    Esta función agrega una posición de clasificación a cada jugador en una lista basada en sus puntos
    totales, rebotes, asistencias y robos, y devuelve una cadena formateada con el nombre del jugador y
    su clasificación en cada categoría.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
     sus estadísticas. Ademas, a cada diccionario se le agrega claves cuyo nombre son los elementos, 
     con un replace, de lista_datos.
    :type lista_jugadores: list
    :return: una cadena que contiene una lista separada por comas de las estadísticas de los jugadores.
    """
    
    lista_datos = ['puntos_totales', 'rebotes_totales', 'asistencias_totales', 'robos_totales']
    for dato in lista_datos:
        lista_ordenada = ordenar_estadistica_dato_descendente(lista_jugadores, dato)

        for i in range(len(lista_ordenada)):
            lista_ordenada[i][dato.replace('_totales', "")] = i+1

    lista_contenido = ['Jugador,Puntos,Rebotes,Asistencias,Robos']

    for jugador in ordenar_palabras(lista_ordenada, 'nombre', False):
        lista_contenido.append('{0},{1},{2},{3},{4}'.format(jugador['nombre'], jugador['puntos'], jugador['rebotes'], jugador['asistencias'], jugador['robos']))

    return join_lista(lista_contenido, True)

#EJERCICIO 22
def cantidad_jugadores_por_posicion(lista_jugadores: list) -> str:
    '''
    Recibe una lista de jugadores como parametro que contiene la informacion un jugador por cada diccionario.
    Crea un diccionario donde iran la cantidad de jugadores que hay en cada posicion
    Devuelve un string con el nombre de la posicion y la cantidad de jugadores de la lista que tiene cada una
    retorna un string
    '''
    diccionario_posicion = {}
    for jugador in lista_jugadores:
        if jugador['posicion'] in diccionario_posicion:
            diccionario_posicion[jugador['posicion']] += 1
        else:
            diccionario_posicion[jugador['posicion']] = 1

    lista_cantidad_posicion = []

    for clave, valor in diccionario_posicion.items():
        lista_cantidad_posicion.append('{0}: {1}'.format(clave, valor))

    return join_lista(lista_cantidad_posicion, True)

#EJERCICIO 23
def cantidad_all_star(lista_jugadores: list) -> list:
    """
    Recibe una lista de jugadores como parametro que contiene la informacion un jugador por cada diccionario.
    Esta función toma una lista de jugadores y sus logros, los ordena por el número de logros All-Star
    que tienen devuelve una cadena formateada de los nombres de los jugadores y sus logros All-Star.
    Retorna un string
    """
    
    for jugador in lista_jugadores:
        for elemento in jugador['logros']:
            if re.search(r'All-Star', elemento):
                jugador['Star'] = re.search(r'(\d+)', elemento).group()

    rango = len(lista_jugadores[:-1])
    flag_swap = True
    while flag_swap:
        flag_swap = False
        rango -= 1
        for i in range(rango):
            if int(lista_jugadores[i]['Star']) < int(lista_jugadores[i+1]['Star']):
                lista_jugadores[i], lista_jugadores[i+1] = lista_jugadores[i+1], lista_jugadores[i]
                flag_swap = True

    lista = []
    for jugador in lista_jugadores:
        for elemento in jugador['logros']:
            if re.search(r'All-Star', elemento):
                lista.append('{0} ({1})'.format(jugador['nombre'], elemento))
    return join_lista(lista, True)                          

#EJERCICIO 24
def imprimir_mayores_estadisticas(lista_jugadores: list) -> str:
    '''
    Recibe una lista de jugadores como parametro que contiene la informacion un jugador por cada diccionario.
    Determina el jugador tiene las mejores estadísticas en cada valor.
    Devuelve un string con el los nombres de los que tienen el mayor numero de cada estadistca con su respectivo valor
    retonna un string
    '''
    lista = []
    lista_datos = ["temporadas", "puntos_totales", "rebotes_totales", "promedio_rebotes_por_partido", "asistencias_totales", "promedio_asistencias_por_partido"
                   "robos_totales", "bloqueos_totales", "porcentaje_tiros_de_campo", "porcentaje_tiros_libres", "porcentaje_tiros_triples"]
    for dato in lista_datos:
       for jugador in calcular_jugador_mayor_estadistica_dato(lista_jugadores, dato):
        lista.append('Mayor cantidad de {0}: {1} ({2})'.format(normalizar_dato(dato), jugador['nombre'], jugador['estadisticas'][dato]))

    return join_lista(lista, True)  

#EJERCICIO 25
def jugador_con_mayor_estadistica(lista_jugadores: list) -> str:
    '''
    Recibe una lista de jugadores como parametro que contiene la informacion un jugador por cada diccionario.
    Acumula todos los valores de las estadisticas y devuelve cual es el jugador que mas valor acumulo
    retoran un string
    '''
    acumulador_estadistica = 0

    for indice in range(len(lista_jugadores)):
        for valor in lista_jugadores[indice]['estadisticas'].values():
            acumulador_estadistica += valor

        if indice == 0 or acumulador_estadistica > max_estadistica:
            max_estadistica = acumulador_estadistica
            indice_max = indice
        
    cadena = 'El jugador con la mayor estadistica es: {0}'.format(lista_jugadores[indice_max]['nombre'])
    return cadena

def imprimir_menu() -> None:
    '''
    Muestra el menu de opciones
    Return: None
    '''
    print('----------------------------------------------------------MENU DE OPCIONES------------------------------------------------------------')
    print('1.  Mostrar la lista de todos los jugadores del Dream Team.')
    print('2.  Mostrar a estadisticas de un jugador por input.')
    print('3.  Guardar las estadísticas del jugador ingresado en el punto anterior en un archivo CSV.')
    print('4.  Mostrar a estadisticas de un jugador por input.')
    print('5.  Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.')
    print('6.  Mostrar si el jugador ingresado por input es miembro del Salón de la Fama del Baloncesto.')
    print('7.  Mostrar el jugador con la mayor cantidad de rebotes totales.')
    print('8.  Mostrar el jugador con el mayor porcentaje de tiros de campo.')
    print('9.  Mostrar el jugador con la mayor cantidad de asistencias totales.')
    print('10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.')
    print('11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.')
    print('12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.')
    print('13. Mostrar el jugador con la mayor cantidad de robos totales.')
    print('14. Mostrar el jugador con la mayor cantidad de bloqueos totales.')
    print('15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.')
    print('16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.')
    print('17. Mostrar el jugador con la mayor cantidad de logros obtenidos.')
    print('18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.')
    print('19. Mostrar el jugador con la mayor cantidad de temporadas jugadas.')
    print('20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.')
    print('21. Crear tabla de posiciones (por puntos, rebotes, asistencias y robos), ordenada por nombre en orden alfabetico.')
    print('22. Mostrar la cantidad de jugadores que hay por cada posición.')
    print('24. Mostrar qué jugador tiene las mejores estadísticas en cada valor.')
    print('25. Mostrar qué jugador tiene las mejores estadísticas de todos.')
    print('0.  Salir. ')
    print('--------------------------------------------------------------------------------------------------------------------------------------')

def validar_numero(numero: str) -> int:
    '''
    Recibe una variable string numerica.
    Verifica si el valor ingresado es un numero o no
    Retorna un input
    '''
    while not re.match(r'^[0-9]+$', numero):
        numero = input('[ERROR]Ingrese numero: ')
    return int(numero)

def validar_indice() -> int:
    '''
    El código anterior solicita al usuario que ingrese un número entre 1 y 12, y luego verifica si
    la entrada es un número entero válido dentro de ese rango. Si la entrada es válida, el código
    devuelve la entrada como un número entero. El código se ejecuta en un bucle infinito hasta que
    se proporciona una entrada válida.
    '''
    while True:
        indice = input("Ingrese un número entre 1 y 12: ")
        if indice.isdigit():
            numero = int(indice)
            if 1 <= numero <= 12:
                return numero

def validar_nombre(lista_jugadores: list) -> list:
    """
    Esta función toma una lista de jugadores y solicita al usuario que ingrese letras para buscar
    nombres de jugadores coincidentes, devolviendo una lista de jugadores cuyos nombres contienen las
    letras ingresadas.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene información sobre un jugador, como su nombre, edad, etc
    :type lista_jugadores: list
    :return: una lista de diccionarios que contienen los jugadores cuyos nombres coinciden con la
    entrada proporcionada por el usuario. Si no se encuentran coincidencias, la función devuelve una
    lista vacía.
    """
    nombres_coincidentes = []
    contador_coincidencias = 0

    while True:
        letras_ingresadas = input("Ingresar nombre o parte del nombre: ").lower()

        if re.match('^[a-z ]+$', letras_ingresadas):
            for jugador in lista_jugadores:
                if letras_ingresadas in jugador["nombre"].lower():
                    contador_coincidencias += 1
                    nombres_coincidentes.append(jugador)

            if nombres_coincidentes:
                print('Coincidencias encontradas: {0}\n'.format(contador_coincidencias))
                return nombres_coincidentes

            print("No se encontraron nombres coincidentes. Vuelva a ingresar otro")
            input('PULSE ENTER PARA CONTINUAR')

        print("Entrada inválida. Ingresar solo letras.")
        input('PULSE ENTER PARA CONTINUAR')

def main_dream_team(lista_jugadores: list) -> None:
    '''
    Recibe como parametro la lista de diccionarios con informacion de cada jugador del DreamTeam
    Llama a la funcion imprimir_menu y permite acceder a las funciones dependiendo de la opcion ingresada
    Return none
    '''
    flag_main = True
    flag_guardar = False
    while flag_main:
        imprimir_menu()
        opcion = validar_numero(input('Ingrese numero de opcion (0 al 20): '))
        match opcion:
            case 0:
                flag_main = False
            case 1:
                print('')
                print(mostrar_jugadores_nombre_posicion(lista_jugadores, True))
                input('PULSE ENTER PARA CONTINUAR')
            case 2:
                indice_input = validar_indice()
                opcion_dos = mostrar_estadisticas(lista_jugadores, indice_input)
                flag_guardar = True
                input('PULSE ENTER PARA CONTINUAR')
            case 3:
                if flag_guardar:
                    guardar_csv('{} estadisticas.csv'.format(lista_jugadores[indice_input-1]['nombre']), opcion_dos)
                else:
                    print('Primero ingrese a la opcion 2')
                input('PULSE ENTER PARA CONTINUAR')
            case 4:
                print(' ')
                mostrar_si_pertenece_salon_fama(validar_nombre(lista_jugadores), False)
                input('PULSE ENTER PARA CONTINUAR')
            case 5:
                dato = 'promedio_puntos_por_partido'
                print(cadena_promedio_total(dato, calcular_promedio_puntos_por_partido(lista_jugadores, dato), True))
                print(mostrar_jugadores_nombre_posicion(ordenar_palabras(lista_jugadores, 'nombre', False), False))
                input('PULSE ENTER PARA CONTINUAR')
            case 6:
                mostrar_si_pertenece_salon_fama(validar_nombre(lista_jugadores), True)
                input('PULSE ENTER PARA CONTINUAR')
            case 7:
                mostrar_jugador_estadistica_dato(calcular_jugador_mayor_estadistica_dato(lista_jugadores, 'rebotes_totales'), 'rebotes_totales')
                input('PULSE ENTER PARA CONTINUAR')
            case 8: 
                mostrar_jugador_estadistica_dato(calcular_jugador_mayor_estadistica_dato(lista_jugadores, 'porcentaje_tiros_de_campo'), 'porcentaje_tiros_de_campo')
                input('PULSE ENTER PARA CONTINUAR')
            case 9:
                mostrar_jugador_estadistica_dato(calcular_jugador_mayor_estadistica_dato(lista_jugadores, 'asistencias_totales'), 'asistencias_totales')
                input('PULSE ENTER PARA CONTINUAR') 
            case 10:
                numero_puntos = validar_numero(input('Ingrese valor: '))
                print(mayor_cantidad_dato(lista_jugadores, 'promedio_puntos_por_partido', numero_puntos))
                input('PULSE ENTER PARA CONTINUAR')
            case 11:
                numero_rebores = validar_numero(input('Ingrese valor: '))
                print(mayor_cantidad_dato(lista_jugadores, 'promedio_rebotes_por_partido', numero_rebores))
                input('PULSE ENTER PARA CONTINUAR')
            case 12:
                numero_asistencias = validar_numero(input('Ingrese valor: '))
                print(mayor_cantidad_dato(lista_jugadores, 'promedio_asistencias_por_partido', numero_asistencias))
                input('PULSE ENTER PARA CONTINUAR')
            case 13:
                mostrar_jugador_estadistica_dato(calcular_jugador_mayor_estadistica_dato(lista_jugadores, 'asistencias_totales'), 'rebotes_totales')
                input('PULSE ENTER PARA CONTINUAR')
            case 14:
                mostrar_jugador_estadistica_dato(calcular_jugador_mayor_estadistica_dato(lista_jugadores, 'bloqueos_totales'), 'bloqueos_totales')
                input('PULSE ENTER PARA CONTINUAR') 
            case 15:
                numero_tiros_libres = validar_numero(input('Ingrese valor: '))
                print(mayor_cantidad_dato(lista_jugadores, 'porcentaje_tiros_libres', numero_tiros_libres))
                input('PULSE ENTER PARA CONTINUAR')
            case 16:
                dato = 'promedio_puntos_por_partido'
                promedio = calcular_promedio_puntos_por_partido(ordenar_estadistica_dato_descendente(lista_jugadores, dato)[:-1], dato)
                print(cadena_promedio_total(dato, promedio, False))
                input('PULSE ENTER PARA CONTINUAR')
            case 17:
                print(jugador_con_mas_logros(lista_jugadores))
                input('PULSE ENTER PARA CONTINUAR')
            case 18:
                numero_tiros_triples = validar_numero(input('Ingrese valor: '))
                print(mayor_cantidad_dato(lista_jugadores, 'porcentaje_tiros_triples', numero_tiros_triples))
                input('PULSE ENTER PARA CONTINUAR')
            case 19:
                mostrar_jugador_estadistica_dato(calcular_jugador_mayor_estadistica_dato(lista_jugadores, 'temporadas'), 'temporadas')
                input('PULSE ENTER PARA CONTINUAR')
            case 20:
                numero_tiros_campo = validar_numero(input('Ingrese valor: '))
                print(mayor_cantidad_dato(ordenar_palabras(lista_jugadores, 'posicion', False), 'porcentaje_tiros_de_campo', numero_tiros_campo))
                input('PULSE ENTER PARA CONTINUAR')
            case 21:
                guardar_csv('Ranking_posiciones.csv', agregar_posicion_ranking_dato(lista_jugadores))
                input('PULSE ENTER PARA CONTINUAR')
            case 22:
                print(cantidad_jugadores_por_posicion(lista_jugadores))
                input('PULSE ENTER PARA CONTINUAR')
            case 23:
                print(cantidad_all_star(lista_jugadores))   
                input('PULSE ENTER PARA CONTINUAR')
            case 24:
                print(imprimir_mayores_estadisticas(lista_jugadores))
                input('PULSE ENTER PARA CONTINUAR')
            case 25:
                print(jugador_con_mayor_estadistica(lista_jugadores))
                input('PULSE ENTER PARA CONTINUAR')
            case _:
                print('Opcion no valida.')
                input('PULSE ENTER PARA CONTINUAR')

main_dream_team(lista_jugadores = leer_archivo('C:\\Users\\enzo9\\OneDrive\\Documentos\\Programacion 1\\def\\dt.json'))