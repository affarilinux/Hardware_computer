

class Pagina:
    # Atributo de classe (compartilhado por todas as instâncias)
    pag = None

    @classmethod
    def setpag(cls, page):
        cls.pag = page

    @classmethod
    def getpag(cls):
        return cls.pag
        