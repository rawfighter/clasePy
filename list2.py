def comandos(valor):
    if  valor == "salir":
        return False
    elif valor == "remueve primero":
        nombres.remove(nombres[0])
    elif valor == "remueve ultimo":
        nombres.remove(nombres[len(nombres)-1])
    else:
        nombres.append(valor)
    return True

def resultado(valor):
    for n in nombres:
        print(n)
   
nombres = []
control = True
while(control):
    valor = input("Dame un nombre ")
    control = comandos(valor)

resultado(nombres)