def esAoZ(coleccion):
    if len(coleccion) > 0:
        if coleccion [0] == 'A' or coleccion[0] == "z":
            return True
        else:
            return False
    else:
        return False
print(esAoZ("Ronald"))
print(esAoZ("Mileyshka"))
print(esAoZ("Angie"))