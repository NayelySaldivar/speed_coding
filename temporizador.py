import time
import threading
import sys 

def temporizador(tiempo):
    global tiempo_restante
    tiempo_restante = tiempo
    for i in range(tiempo):
        tiempo_restante = tiempo_restante - 1
        time.sleep(1)

    mensaje_fin="\n\n--------FIN DEL TIEMPO-------\n\n"

    for char in mensaje_fin:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

    mensaje_enter="Presiona ENTER.\n"

    for char in mensaje_enter:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.005)
