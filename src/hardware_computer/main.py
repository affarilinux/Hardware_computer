from flet import run, Page

from core.ultils.pag import Pagina

#center
from center.index_ import Index
from center.padrao_pagina import PadraoPagina

class AppMain:
    """
    Classe principal que inicia o aplicativo.
    """

    def __init__(self, page: Page) -> None:
        self.pageinit = page
        
        #def pagina_init()
        self.ct_class_padrao_pagina = PadraoPagina()
        self.ct_class_index = Index()

        self.pagina_init()

        self.pageinit.update()

    def pagina_init(self):

        Pagina.setpag(self.pageinit)
        
        self.ct_class_padrao_pagina.tamanho_tela(self.pageinit)
        self.ct_class_padrao_pagina.cor_fundo_pagina(self.pageinit)

        self.pageinit.update()

        self.ct_class_index.sistema()

        


def main(page: Page) -> None:

    AppMain(page)


if __name__ == "__main__":
    run(main)