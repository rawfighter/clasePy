def linearSearch(lista, objeto):
     for indice in range(len(lista)):
          if(lista[indice] == objeto):
               return indice
lista= ["carro","bote","avion","tren"]
print(linearSearch(lista, "bote")) 