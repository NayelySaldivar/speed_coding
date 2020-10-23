from mensaje_inicial import mensaje_inicial
from puntaje import *
from temporizador import *
from claseregex import *

if __name__ == "__main__":
    if mensaje_inicial() == True: #Si el usuario quiere jugar.  
        
        # Iniciar puntaje: se inició desde la importación. 
        # Mensaje: cuenta regresiva para iniciar.
        print("3...")
        time.sleep(1)
        print("Recuerda escribir tu expresión SIN COMILLAS!")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("Puedes saltar la pregunta escribiendo 'skip' :)")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("¡Adelante!")
                
        # Iniciar temporizador. La parte de "args" es para ponerle el tiempo
        thread_temporizador = threading.Thread(target = temporizador, args=(5, ))
        thread_temporizador.start()

        # Mostrar preguntas mientras siga activo el contador.
        while thread_temporizador.is_alive():
            
            #Inicializamos las preguntas
            cuestionario=Preguntas(1,2,3,4)
            cuestionario.prueba()
#             print('')
            time.sleep(1)

        # Terminar la ronda

        # Preguntar si quiere volver a jugar
        pregunta=input("¿Quieres jugar de nuevo?")
        time.sleep(1)
        
    else: # Si la persona ya se quiere salir.
        print("\n¡Regresa pronto!\n")
        time.sleep(0.1)


#