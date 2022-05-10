from decorator import decorator

class Flask():
    def __init__(self):
        self.rotas = dict()

    def rota(self, path):
        def decorator(f):
            self.rotas[path] = f
            return f

        return decorator

    def executar(self, path, *args, **kwargs):
        if path not in self.rotas:
            return 404
        f = self.rotas[path]
        return f(*args, **kwargs)