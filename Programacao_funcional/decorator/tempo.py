from functools import wraps
from time import sleep, strftime
from decorator import decorator


@decorator
def logar(f, fmt='%H:%M:%S', *args, **kwargs):
    print(strftime(fmt))
    return f(*args, **kwargs)


@logar()
def mochileiro():
    return 40


@logar(fmt='%d/%m/%Y %H:%M:%S')
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
