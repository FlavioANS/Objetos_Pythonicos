from functools import wraps
from time import sleep, strftime


def logar(f):
    @wraps(f)
    def executar_com_tempo(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*args, **kwargs)

    return executar_com_tempo


@logar
def mochileiro():
    return 40

@logar
def ola(nome):
    return f'Ola {nome}'


if __name__ == '__main__':
    print(mochileiro())
    print(mochileiro.__name__)
    print(ola('Flavio'))
    print(ola.__name__)
    sleep(2)
    print(mochileiro())
    print(ola('maria'))