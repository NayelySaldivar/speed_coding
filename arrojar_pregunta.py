import random
import re
from preguntas import *
from launcher import *
from mensaje_con_delay import *


def arrojar_pregunta(thread_temporizador, p_restantes):
    # Seleccionar la pregunta que se utilizará
    num_pregunta = random.choice(p_restantes)
    
    # Borrar la pregunta seleccionada de la lista de preguntas_restantes
    p_restantes = p_restantes.remove(num_pregunta)

    # Iniciar pregunta y contador de intentos
    pregunta_activa = True
    intentos = 0
    
    while pregunta_activa:
        
        # Imprimir la pregunta seleccionada
        mensaje = u"\nPregunta: " + todas_las_preguntas[num_pregunta-1].pregunta
        mensaje_con_delay(mensaje, 0, 0)

        # Imprimir ayuda si ya lleva varios intentos
        if intentos == 2:
            pista = "\nPista: " + todas_las_preguntas[num_pregunta-1].ayuda 
            mensaje_con_delay(pista)

        #Pedir respuesta del usuario
        respuesta = input('\n>>> ')

        # Pasar respuesta a formato regex
        try:
            resp_regex = re.compile("^"+respuesta+"$")
        
        # Checar respuesta del usuario
            match = re.search(resp_regex,todas_las_preguntas[num_pregunta-1].respuesta)

            if not thread_temporizador.is_alive():
                pregunta_activa = False

            elif respuesta == 'skip':
                pregunta_activa = False

            elif match:
                print(u'\u001b[38;5;84m' + '¡Correcto!' + u'\u001b[0m')
                pregunta_activa = False

            else:
                print(u'\u001b[38;5;209m' + 'Inténtalo nuevamente :(' + u'\u001b[0m')
                intentos += 1
        
        except:
            print(u'\u001b[38;5;213m' + 'Esa no es una expresión regular.' + '\u001b[0m')
            if not thread_temporizador.is_alive():
                pregunta_activa = False
         
    return 0 if (respuesta == 'skip') or (not thread_temporizador.is_alive()) else 1 