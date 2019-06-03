#!arbol
def manipulador(comando):
    if(comando == "arbol"):
        print(    "    /\ ")
        print(   "    /  \ ")
        print(  "    /    \ ")
        print( "    /      \ ")
    elif comando == "feliz":
         print(":)")

manipulador("arbol")
manipulador("feliz")
valor = input("que quieres?")
manipulador(valor)