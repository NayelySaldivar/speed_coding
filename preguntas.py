from Clase_pregunta import Pregunta

p1 = Pregunta(2,"Expresión que utilizarías para hacer match con 'ABCDEFabcdef123450' ",'ABCDEFabcdef123450',"Considera letras y números")
p2 = Pregunta(1,"Haz match con '@ironhackmexico'","@ironhackmexico","No olvides el @")
p3 = Pregunta(1,"Considerando 27-03-1996 ¿Qué usarías para regresar la fecha?" ,"27-03-1996","Recuerda usar '\' para especificar")
p4 = Pregunta(2,"Haz match con '#insta<3U'","#insta<3U","Considera todos los caracteres especiales")
p5 = Pregunta(1,"Expresión que utilizarías para obtener un string con los primeros 10 caracteres de la CURP","SARN960327","Recuerda que se compone de 4 letras y 6 números!")

# Las juntamos en una lista para poder después hacer index
todas_las_preguntas = [p1, p2, p3, p4, p5]