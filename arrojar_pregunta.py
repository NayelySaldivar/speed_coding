import random
import re
from preguntas import *

preguntas_restantes = [1, 2, 3, 4, 5]
num_pregunta_usuario = 0

def arrojar_pregunta():
    # Seleccionar la pregunta que se utilizará
    global preguntas_restantes
    num_pregunta = random.choice(preguntas_restantes)
    
    # Borrar la pregunta seleccionada de la lista de preguntas_restantes
    preguntas_restantes.remove(num_pregunta)

    # Registrar en qué pregunta va el usuario
    global num_pregunta_usuario
    num_pregunta_usuario += 1

    # Iniciar pregunta
    global thread_temporizador
    pregunta_activa = True
    intentos = 0
    while pregunta_activa:
        
        # Imprimir la pregunta seleccionada
        print(f"\nPregunta {num_pregunta_usuario}:", todas_las_preguntas[num_pregunta-1].pregunta)

        # Imprimir ayuda si ya lleva varios intentos
        if intentos == 2:
            print("Pista:",todas_las_preguntas[num_pregunta-1].ayuda) 

        #Pedir respuesta del usuario
        respuesta = input('>>>')

        # Pasar respuesta a formato regex
        resp_regex = exp_reg = re.compile("'^"+respuesta+"$'")
        
        # Verificar si la respuesta está en el string que se indicó
        match = resp_regex.search(todas_las_preguntas[num_pregunta-1].respuesta)

        # Checar respuesta del usuario
        if respuesta == 'skip':
           pregunta_activa = False

        elif respuesta == 'correcta':
            print('¡Correcto!')
            puntaje += 1
            pregunta_activa = False

        else:
            print('Inténtalo nuevamente :(')
            intentos += 1