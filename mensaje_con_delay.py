import time
import sys

def mensaje_con_delay(mensaje, delay_mensaje=0.015, delay_post=0):
    for char in mensaje:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_mensaje)

    time.sleep(delay_post)