import json
import re

def leer_archivo(ruta: str) -> list:
    '''
    
    '''
    with open(ruta, 'r', encoding = 'utf-8') as archivo:
        contenido = json.load(archivo)

    return contenido['jugadores']
lista_jugadores = leer_archivo('C:\\Users\\enzo9\\OneDrive\\Documentos\\Programacion 1\\def\\dt.json')

def chequear_lista(lista_jugadores: list) -> bool:
    if len(lista_jugadores) > 0:
        flag_lista = True
    else:
        flag_lista = False
    return flag_lista 
def mostrar_jugadores_nombre_posicion(lista_jugadores: list) -> str:
    mensaje = ''
    for jugador in lista_jugadores:
        mensaje += '{0} - {1}\n'.format(jugador['nombre'], jugador['posicion'])
    return print(mensaje)
#mostrar_jugadores_nombre_posicion(lista_jugadores)

def mostrar_estadisticas(lista_jugadores: list, input: int) -> str:
    mensaje = ''
    for indice in range(len(lista_jugadores)):
        if input == indice + 1:
            estadisticas = lista_jugadores[indice]['estadisticas']
            nombre = '----------{0}---------\n\nPOSICION: {1}\n\nESTADISTICAS:\n'.format(lista_jugadores[indice]['nombre'], lista_jugadores[indice]['posicion'])
            for clave, valor in estadisticas.items():
                mensaje += '{1}: {2} \n'.format(nombre, clave.capitalize().replace('_', " "), valor)
    return nombre + mensaje
print(mostrar_estadisticas(lista_jugadores, 2))

def guardar_csv(ruta: str,  contenido: str) -> bool:
    with open(ruta, 'w+') as archivo:
        byte = archivo.write(contenido)
    if byte > 0:
        flag_creado = True
    else:
        flag_creado = False
    return flag_creado

def mostrar_logros_por_nombre(lista_jugadores: list, input: str):
    mensaje = ''
    for jugador in lista_jugadores:
        if input == jugador['nombre']:
            nombre = '----------{0}---------\n\nLOGROS:\n'.format(jugador['nombre'])
            for indice in jugador['logros']:
                mensaje += indice + '\n'
    return nombre + mensaje
#print(mostrar_logros_por_nombre(lista_jugadores, 'Michael Jordan'))

def dividir(numerador: float, divisor: int) -> float:
    '''
    recibe una variable float y otra int
    verifica que el denominador sea distindo de 0
    retorna la divisione de las dos variables
    '''
    if divisor == 0:
        return 0
    else:
        return numerador / divisor           

def sumar_dato(lista_jugadores: list, dato: str) -> float:
    '''
    recibe una lista y un string como parametro
    acumula los valores dependiendo del dato ingresado
     
    '''
    acumulador_dato = 0
    if len(lista_jugadores) > 0:
        for jugador in lista_jugadores:
            for estadistca in jugador['estadisticas']:
                acumulador_dato += estadistca['promedio_puntos_por_partido']
    else: 
        print('ERROR LISTA')
    return acumulador_dato
#'promedio_puntos_por_partido'

def calcular_promedio(lista:list, dato:str)->float:
    '''
    recibe una lista y un string como parametros
    calcula el promedio y lo redondea con 2 decimales
    retorna un float
    '''
    retorno = dividir(sumar_dato(lista, dato), len(lista))
    retorno_redondeado = round(retorno, 2)
    return retorno_redondeado
#print(calcular_promedio(lista_jugadores, 'promedio_puntos_por_partido'))