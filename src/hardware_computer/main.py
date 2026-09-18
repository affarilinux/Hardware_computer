from flet import run, Page

from core.ultils.pag import Pagina

#views
from views.index_ import Index
from views.padrao_pagina import PadraoPagina

class AppMain:
    """
    Classe principal que inicia o aplicativo.
    """

    def __init__(self, page: Page) -> None:
        self.pageinit = page
        self.pagina_init()

        self.pageinit.update()

    def pagina_init(self):

        Pagina.setpag(self.pageinit)
        

        var_padrao_pagina = PadraoPagina()
        var_padrao_pagina.tamanho_tela(self.pageinit)
        var_padrao_pagina.cor_fundo_pagina(self.pageinit)

        self.pageinit.update()

        var_index = Index()
        var_index.sistema_asyncio()

        


def main(page: Page) -> None:

    AppMain(page)


if __name__ == "__main__":
    run(main)