from mensaje_inicial import mensaje_inicial
from puntaje import *
from temporizador import *
from claseregex import *
from cuenta_regresiva import *
from arrojar_pregunta import *

if __name__ == "__main__":
    if mensaje_inicial() == True: #Si el usuario quiere jugar.  
        
        # Iniciar puntaje: se inició desde la importación. 
        # Mensaje: cuenta regresiva para iniciar.
        cuenta_regresiva()
                
        # Iniciar temporizador. La parte de "args" es para ponerle el tiempo
        thread_temporizador = threading.Thread(target = temporizador, args=(20, ))
        thread_temporizador.start()

        # Mostrar preguntas mientras siga activo el contador.
        while thread_temporizador.is_alive():
            arrojar_pregunta()

        # Terminar la ronda

        # Preguntar si quiere volver a jugar
        pregunta = input("¿Quieres jugar de nuevo?")
        time.sleep(1)
        
    else: # Si la persona ya se quiere salir.
        print("\n¡Regresa pronto!\n")
        time.sleep(0.1)


#
