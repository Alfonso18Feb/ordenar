# # ejercicio ordenar tareas pero solo las termnadas y las que no se tienen que terminar antes de de ordenar

"""
el INPUT NOS DICE SI LA TAREA YA ESTA HECHA CON UN 1 Y SI NO ESTA HECHA LA TAREA TIENE UN 0 EN EL
DICIONARIO
"""

lista1 = {'desayuno': 1, 'merienda': 0, 'comida': 0, 'almuerzo': 0, 'cena': 0}
"""
Ya ESTA ORDENADA CASI ORDENADA SOLO NOS HACE FALTA COMPLETAR LAS TAREAS PARA ASI PODER
ORDENAR que es lo que comemos primero por orden de priridad
"""
def comer(lista1,n=0):
    for tarea,clave in lista1.items():#para cada tarea y clave tenemos que recorrer la lista
        if clave == 0:#si la clve es 0 
            lista1[tarea]= 1#cambiamos la tarea a completada con 1
            for valor in lista1.values():
                if valor == 0:#si tenemos un cero es un TRUE
                    cero_encontrado = True
                else:#sino es false
                    cero_encontrado = False
            while cero_encontrado==False:#hago un while para recorerlo las infinitas veces para hacer que las tareas esten completas y ordenadas
                #luego este bucle for compruva si el valor de las listas estan compltas
                #Si no hacemos recursividad para ir al siguiente valos
                for tarea,valor in lista1.items():
                    if valor==1:
                        return lista1
                    else:
                        comer(lista1,n+1)

"""
Alfinal tenemos el output del algoritmo donde te aparece ordenada la comida en orden del tiempo cuando la comes de más temprano a más tarde

"""

print(comer(lista1))

