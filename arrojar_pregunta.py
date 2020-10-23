import random
import re
from preguntas import *
from launcher import *

num_pregunta_usuario = 0

def arrojar_pregunta(thread_temporizador, p_restantes):
    # Seleccionar la pregunta que se utilizará
    num_pregunta = random.choice(p_restantes)
    
    # Borrar la pregunta seleccionada de la lista de preguntas_restantes
    p_restantes = p_restantes.remove(num_pregunta)

    # Iniciar pregunta
    pregunta_activa = True
    intentos = 0
    while pregunta_activa:
        
        # Imprimir la pregunta seleccionada
        print(f"\nPregunta:", todas_las_preguntas[num_pregunta-1].pregunta)

        # Imprimir ayuda si ya lleva varios intentos
        if intentos == 2:
            print("Pista:",todas_las_preguntas[num_pregunta-1].ayuda) 

        #Pedir respuesta del usuario
        respuesta = input('>>>')

        # Pasar respuesta a formato regex
        resp_regex = re.compile('^'+respuesta+'$')
        
        # Checar respuesta del usuario
        match = re.search(resp_regex, todas_las_preguntas[num_pregunta-1].respuesta)

        if not thread_temporizador.is_alive():
            pregunta_activa = False

        elif respuesta == 'skip':
           pregunta_activa = False

        elif match:
            print('¡Correcto!')
            pregunta_activa = False

        else:
            print('Inténtalo nuevamente :(')
            intentos += 1