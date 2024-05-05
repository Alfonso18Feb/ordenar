'''
Este algoritmo ordena la lista permutamdo las filas empezando por los primeros dos pares
'''
#el input del algoritmo es una lista con numeros enteros: En verde esta si tu quieres hacer tu propia lista
# vector=input('Escribe tu lista: ').split()
# vector = list(map(int, vector))
vector=[1,2,3,3,4,2,3,4,2,2,3,2]
"""
En esta funcion tenemos condiciones para ver si esta ordenado de mayor a menor
Con la variable n=0 para indicar que empezamos por el indice del vector cero
Y comparamos cada una hasta llegar un momento donde o son iguales o los menores estan primero
"""
def ordenar(vector, n=0):
    if n >= len(vector) - 1:#si hay un elemento ya estaria ordenado
        return vector
    
    elif vector[n] > vector[n + 1]:#cuando hay dos elementos del vector y el primero es mayos que el segundo
        vector[n], vector[n + 1]=vector[n+1],vector[n]#los intercambio
        return ordenar(vector)#luego volvemos a ordenar pero con los vectores intercambiados
    else:
        return ordenar(vector, n + 1)#Si los dos vectores son ya iguales o el menor va primero ahora volvemos ha ordenar pero esta vez con n+1(2,3,4,...)
"""
El output del algoritmo es simple devuelve el vector ordenado
"""
print('lista ordenada por dictomia es: \n',ordenar(vector))