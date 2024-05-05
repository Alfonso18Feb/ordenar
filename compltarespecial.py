'el input del algoritmo es sencillo solo es una lista de numeros enters '
Vector=[1,2,3,34, 4,5,4,6,3]
"""
La funcion del algoritmo ordenar es bastate compleja:
Pero es muy simple:
Primero la condicion para ver si podemos dividir la lista en dos segmentos.Si no podemos entonces n=0
Sino:
Dividimos el Vector en dos segmentos
calculamos el maximo de los dos segmentos
Eliminamos los dos maximos de los segmentos
Lugo los comparamos y los añadimos a el vector de menor a Mayor
Finalmente tenemos Unas condiciones donde si el maximo de toda la lista esta en el final
Lo eliminamos del Vector y hacemos un print para que aparezca en pantalla
Entonces por recursividad coremos esta funcion pero esta vez con el vector sin el maximo del principio


Esto continua hasta que los numeros maximos esten en lo alto y los pequeños abajo

"""
def ordenar(Vector):
    n=(len(Vector))//2
    if n==0:
        print(Vector)
    else:
        z=len(Vector)
        list1=Vector[0:n]
        lista2 = Vector[n:]
        x=max(list1)
        y=max(lista2)
        Vector=lista2+list1
        Vector.remove(x)
        Vector.remove(y)
        elementos_eliminados = [x, y]
        elementos_eliminados.sort()
        Vector.extend(elementos_eliminados)
        s=max(Vector)
        if Vector[z-1]==s:
            Vector.remove(s)
            print(s)
            return(ordenar(Vector))
        elif Vector[z-1]!=s:
            return(ordenar(Vector))
#El output del algoritmo es sencillo ya que te explica Como funciona este programa muy bien.Y tenemos la lista organizada
print('Está ordenado de mayor a menor \nel valor más grande esta «en lo alto» y abajo esta el [número] encerrado \nque es el más pequeño \n Ahora aparece (NONE) porque ya no puede recorrer la lista más:',ordenar(Vector))