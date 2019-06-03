def bubleSort(lista):
    n = len(lista)
    control = True
    while (control):
        swapped = False
        for indice in range(n):
             if indice == 0:
                continue
             else:
                if lista[indice -1] > lista[indice]:
                    tmp = lista[indice]
                    lista[indice] = lista[indice -1]
                    lista[indice -1] = tmp
                    swapped = True

        if(not swapped):
             control = False

def binarySearch(lista,objeto):
   n = len(lista)
   puntoMedio = n/2
   puntoActivo = puntoMedio
   while(puntoActivo >= 0 or puntoActivo < n):
   if lista[puntoMedio == objeto]:
      return puntoMedio
   elif lista[puntoActivo] < objeto:
      puntoActivo -=1
   elif lista[puntoActivo] > objeto:
      puntoActivo +=1
   return -1

lista2 = [1,4,3,2,1,5,1]
print(lista2)
bubleSort(lista2)
print(lista2)
print(binarySearch(lista , 2))