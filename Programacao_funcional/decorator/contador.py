def fabrica_de_contador():
    _contador = 0
    def contar():
        nonlocal _contador
        _contador += 1
        return _contador

    return contar

contador = fabrica_de_contador()
contador2 = fabrica_de_contador()
print(contador())
print(contador())
print(contador())
print(contador2())
print(contador2())


_contador = 0
def fabrica_de_contador1():
    def contar():
        global _contador
        _contador += 1
        return _contador

    return contar

contador = fabrica_de_contador1()
contador2 = fabrica_de_contador1()
print(contador())
print(contador())
print(contador())
print(contador2())
print(contador2())
