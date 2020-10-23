import random
import re

class Pregunta:
    def __init__(self, dificultad, pregunta, respuesta, ayuda):
        self.dificultad = dificultad
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.ayuda = ayuda
    
    def prueba(self):
        # Obtenemos una lista aleatoria para mostrar las preguntas.
        num_preguntas = [i for i in random.sample(range(0,5),5)]
        for i in num_preguntas:
            b = False
            intentos = 0
            
            # Mientras que la respuesta sea incorrecta o el usuario salte la 
            # pregunta, se mantendrá en el mismo inciso.
            while (b == False) or (answer != 'skip'):
    
                # Mostramos la pregunta y creamos el output al mismo tiempo:
                answer = input(TotalPreguntas[i].pregunta)
    
                # Se valida la respuesta:
                exp_reg = re.compile("'^"+answer+"$'")
                a = exp_reg.search(TotalPreguntas[i].respuesta)
                b = not bool (a)
    
                # Si ya va por el tercer intento, imprime una ayuda para solucionar el inciso:
                intentos+=1
                if intentos == 2:
                    print("Hint: ",TotalPreguntas[i].ayuda) 