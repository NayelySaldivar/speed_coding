from mensaje_inicial import mensaje_inicial
from cuenta_regresiva import *
from temporizador import *
from arrojar_pregunta import *
from mensaje_con_delay import *
from dinosaurios import *

puntos=0

if __name__ == "__main__":
    if mensaje_inicial() == True: #Si el usuario quiere jugar.  
        
        # Mantener el juego activo.
        juego_activo = True
        while juego_activo:
            
            # Mensaje: cuenta regresiva para iniciar.
            cuenta_regresiva()
                    
            # Iniciar temporizador.
            thread_temporizador = threading.Thread(target = temporizador, args=(60, ))
            thread_temporizador.start()

            # Iniciar contadores de preguntas restantes y puntaje
            preguntas_restantes = [1, 2, 4, 5,6,8,9,10,11]

            # Mostrar preguntas mientras siga activo el temporizador.
            while thread_temporizador.is_alive():
                puntos+=arrojar_pregunta(thread_temporizador, preguntas_restantes)

            # Mostrar puntaje 
            
            banner_score = "\n------------------------------\n\n"
            mensaje_con_delay(banner_score, 0.01)

            el_score = u'\u001b[38;5;87m' + u'\u001b[1m' + f'SCORE: {puntos}' + u'\u001b[0m'
            
            mensaje_con_delay(el_score, 0.13, 0.3)

            obtuviste = u'\u001b[38;5;87m' + '\n\nObtuviste un...\n\n' + u'\u001b[0m'
            mensaje_con_delay(obtuviste, 0.05, 1)
            
            if puntos < 2:
                dino_low()

            elif puntos >= 3:
                dino_mid()


            # Preguntar si quiere volver a jugar
            respuesta_activa = True

            while respuesta_activa:
                quieres_jugar = "\n\n¿Quieres jugar de nuevo?"
                mensaje_con_delay(quieres_jugar)
                respuesta = input("\n>>>")

                if respuesta == ('si' or 'sí' or 'Si' or 'Sí' or 'SI' or 'sI'):
                    respuesta_activa = False
                    puntos=0

                elif respuesta == ('no' or 'No' or 'NO' or 'nO'):
                    juego_activo = False
                    respuesta_activa = False

                else: 
                    mensaje_error = '\nNo te entendí. ¿Qué quisiste decir?\n'
                
                    for char in mensaje_error:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.02)
                    time.sleep(0.5)

    else: 
        pass

    # Mensaje cuando la persona ya se va a salir
    mensaje_fin = "\n¡Regresa pronto!\n"
    mensaje_con_delay(mensaje_fin, 0.015, 0.1)
