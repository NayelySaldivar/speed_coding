import random
import re

class Preguntas:
    def __init__(self,dif,pregunta,respuesta,ayuda):
        self.pregunta=pregunta
        self.dif=dif
        self.respuesta=respuesta
        self.ayuda=ayuda
    
    def prueba(self):
        # Obtenemos una lista alatoria para mostrar las preguntas
        question=[i for i in random.sample(range(0,5),5)]
        for i in question:
            b=False
            intentos=0
            # Mientras que la respuesta sea incorrecta ó el usuario salte la pregunta se mantendrá en el mismo inciso
            while b==False or answer!='skip':
    
                # Mostramos la pregunta y creamos el output al mismo tiempo:
                answer=input(TotalPreguntas[i].pregunta)
    
                # Se valida la respuesta:
                exp_reg=re.compile("'^"+answer+"$'")
                a = exp_reg.search(TotalPreguntas[i].respuesta)
                b=not bool (a)
    
                # Si ya va por el tercer intento, imprime una ayuda para solucionar el inciso:
                intentos+=1
                if intentos == 2:
                    print("Hint: ",TotalPreguntas[i].ayuda) 

# Costruimos las preguntas con sus atributos:
p1=Preguntas(2,"Expresión que utilizarías para hacer match con 'ABCDEFabcdef123450' ",'ABCDEFabcdef123450',"Considera letras y números")
p2=Preguntas(1,"Haz match con '@ironhackmexico'","@ironhackmexico","No olvides el @")
p3=Preguntas(1,"Considerando 27-03-1996 ¿Qué usarías para regresar la fecha?" ,"27-03-1996","Recuerda usar '\' para especificar")
p4=Preguntas(2,"Haz match con '#insta<3U'","#insta<3U","Considera todos los caracteres especiales")
p5=Preguntas(1,"Expresión que utilizarías para obtener un string con los primeros 10 caracteres de la CURP","SARN960327","Recuerda que se compone de 4 letras y 6 números!")

# Las juntamos en una lista para poder después hacer index
TotalPreguntas=[p1,p2,p3,p4,p5]