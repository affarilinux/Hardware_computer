'''class Pagina:

    pag = None

    def setpag(self, page):
        self.pag = page
        

    def getpag(self):
        print(self.pag)
        return self.pag'''

class Pagina:
    # Atributo de classe (compartilhado por todas as instâncias)
    pag = None

    @classmethod
    def setpag(cls, page):
        cls.pag = page

    @classmethod
    def getpag(cls):
        return cls.pag
        