"""
>>> def ola():
    print('Ola')

>>> executar(ola)
Ola
>>> executar(ola, 2)
Ola
Ola
>>> excutar(ola, 3)
Ola
Ola
Ola
"""

def executar(f, n=1):
    for _ in range(n):
        f()