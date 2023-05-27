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
lista_jugadores = leer_archivo('C:\\Users\\enzo9\\OneDrive\\Documentos\\Programacion 1\\def\\dt.json')
#EJERCICIO 1
def mostrar_jugadores_nombre_posicion(lista_jugadores: list) -> str:
    '''
    Recibe como parametros una lista de diccionarios que contiene la informacion de cada uno de los jugadores
    Muestra el nombre y la posicion de todos los jugadores.
    Retorna un string.
    '''
    mensaje = ''
    for jugador in lista_jugadores:
        mensaje += '{0} - {1}\n'.format(jugador['nombre'], jugador['posicion'])
    return mensaje

#EJERCICIO 2
def mostrar_estadisticas(lista_jugadores: list, indice_input: int) -> str:
    '''
    Recibe coo parametros una lista de diccionarios que contiene la informacion de cada uno de los jugadores.
    Muestra el nombre, la posicion y las estadisticas del usuario ingresado por input.
    Retorna un string
    '''
    mensaje = ''
    for indice in range(len(lista_jugadores)):
        if indice_input == indice + 1:
            estadisticas = lista_jugadores[indice]['estadisticas']
            nombre = '----------{0}---------\n\nPOSICION: {1}\n\nESTADISTICAS:\n'.format(lista_jugadores[indice]['nombre'], lista_jugadores[indice]['posicion'])
            for clave, valor in estadisticas.items():
                mensaje += '{1}: {2} \n'.format(nombre, clave.capitalize().replace('_', " "), valor)
    return nombre + mensaje

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
        flag_creado = True
    else:
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
    mensaje = ''
    for jugador in lista:
        if flag_nombre:
            if cadena in jugador['logros']:
                print('-{0} es {1}'.format(jugador['nombre'], cadena))
            else:
                print('-{0} no es {1}'.format(jugador['nombre'], cadena))
        else:
            for logro in jugador['logros']:
                mensaje += logro + '\n'
            print('----------{0}---------\n\nLOGROS:\n{1}'.format(jugador['nombre'], mensaje))

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

#PARTE DE LOS EJERCICIOS 5 Y 20
def ordenar_palabras(lista_jugadores: list, key_string: str, flag: bool) -> list:
    """
    Esta función ordena una lista de diccionarios por una cadena de clave específica en orden ascendente
    o descendente.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus atributos
    :type lista_jugadores: list
    :param key_string: El parámetro key_string es una cadena que representa la clave o atributo del
    diccionario en la lista de reproductores que se usarán para ordenar la lista
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
            if flag == False and lista_jugadores[i][key_string][0] > lista_jugadores[i+1][key_string][0] or\
                flag == True and lista_jugadores[i][key_string][0] < lista_jugadores[i+1][key_string][0]:
                lista_jugadores[i], lista_jugadores[i+1] = lista_jugadores[i+1], lista_jugadores[i]
                flag_swap = True

    return lista_jugadores

#EJERCICIOS 7, 8, 9, 13, 14 Y 19
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

def mostrar_jugador_estadistica_dato(lista: list, dato: str) -> None:
    '''
    Recibe como parametros una lista de diccionarios que contiene la informacion de los jugadores y una variable string que representa una
    key del diccionario 'estadisticas'
    Imprime una cadena formateada
    return: None
    '''
    print('\nCoincidencias encontradas: {0}\n'.format(len(lista)))
    for jugador in lista:
            print('Nombre: {0} - {1}: {2}'.format(jugador['nombre'], dato.capitalize().replace('_', " "), jugador['estadisticas'][dato]))
        

        
    

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
    
    cadena_jugadores = ''
    flag_ingreso = False
    for jugador in lista_jugadores:
        for clave, valor in jugador['estadisticas'].items():
            if clave == dato:
                if valor > numero:
                    flag_ingreso = True
                    if dato == 'porcentaje_tiros_de_campo':
                        cadena_jugadores += 'NOMBRE: {0} POSICION: {1} - {2}: {3}\n'.format(jugador['nombre'],
                                                                                            jugador['posicion'],
                                                                                            dato.capitalize().replace('_', " "),
                                                                                             valor)
                    else:
                        cadena_jugadores += 'NOMBRE: {0} - {1}: {2}\n'.format(jugador['nombre'],
                                                                              dato.capitalize().replace('_', " "),
                                                                              valor)
    if flag_ingreso: 
        return cadena_jugadores
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
    cadena = ''
    for i in range(rango):
        if i == indice_max:
            nombre = '----------{0}---------\n\nLOGROS:\n'.format(lista_jugadores[indice_max]['nombre'])
            for logro in lista_jugadores[indice_max]['logros']:
                cadena += logro + '\n'

    return nombre + cadena

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
    print('13. Mostrar el jugador con la mayor cantidad de robos totales')
    print('14. Mostrar el jugador con la mayor cantidad de bloqueos totales.')
    print('15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.')
    print('16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.')
    print('17. Mostrar el jugador con la mayor cantidad de logros obtenidos')
    print('18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.')
    print('19. Mostrar el jugador con la mayor cantidad de temporadas jugadas')
    print('20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.')
    print('0.  EXIT ')
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
    imprimir_menu()
    flag_main = True
    flag_guardar = False
    while flag_main:
        opcion = validar_numero(input('Ingrese numero de opcion (0 al 20): '))
        match opcion:
            case 0:
                flag_main = False
            case 1:
                print('')
                print(mostrar_jugadores_nombre_posicion(lista_jugadores))
                input('PULSE ENTER PARA CONTINUAR')
            case 2:
                indice_input = validar_indice()
                opcion_dos = mostrar_estadisticas(lista_jugadores, indice_input)
                print(opcion_dos)
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
                key_string = 'nombre'
                dato = 'promedio_puntos_por_partido'
                print('El {0} de todo el equipo del Dream Team es: {1}\n'.format(dato.replace('_', " "), calcular_promedio_puntos_por_partido(lista_jugadores, dato)))
                for jugador in  ordenar_palabras(lista_jugadores, key_string, True):
                    for clave, valor in jugador['estadisticas'].items():
                        if clave == dato:
                            print('{0}: {1} - {2}: {3}'.format(key_string.upper(), jugador[key_string], clave.capitalize().replace('_', " "), valor))
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
                promedio = calcular_promedio_puntos_por_partido( ordenar_estadistica_dato_descendente(lista_jugadores, dato)[:-1], dato)
                print('El {0} del equipo excluyendo al jugador que menos puntos tiene: {1}'.format(dato.replace('_', " "), promedio))
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
            case _:
                print('Opcion no valida.')
                input('PULSE ENTER PARA CONTINUAR')

main_dream_team(lista_jugadores = leer_archivo('C:\\Users\\enzo9\\OneDrive\\Documentos\\Programacion 1\\def\\dt.json'))
