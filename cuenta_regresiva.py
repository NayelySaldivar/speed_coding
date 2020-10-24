import time
import sys

def cuenta_regresiva():
   
    mensaje0 = u'\u001b[1m' + "\n\n--------INSTRUCCIONES--------\n" + '\u001b[0m'
    for char in mensaje0:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    time.sleep(0)

    mensaje1 = "\n1. Escribe la expresión que te piden SIN comillas."
    for char in mensaje1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(0)

    mensaje2 = "\n2. Sáltate una pregunta con 'skip'."   
    for char in mensaje2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(0.5)

    print('\n')

    mensaje3 = '    ¿Listo?'
    for char in mensaje3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)

    print("\n\n3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)