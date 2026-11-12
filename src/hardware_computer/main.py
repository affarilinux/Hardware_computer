from flet import run, Page


# core
from core.ultils.pag import Pagina

# center
from center.index_ import Index
from center.padrao_pagina import PadraoPagina

# sqlite
from SQLite_db.core.composicao import SqliteComposicao


class AppMain:
    """
    Classe principal que inicia o aplicativo.
    """

    def __init__(self, page: Page) -> None:
        self.pageinit = page

        self.__sqlite()
        self.__paginas()
        self.__pagina_init()

        self.pageinit.update()

    def __sqlite(self):

        self.mn_class_sqlite = SqliteComposicao()
        self.mn_class_sqlite.tabelas_criacao()
    
    def __paginas(self):

        Pagina.setpag(self.pageinit)

        self.ct_class_padrao_pagina = PadraoPagina()
        self.ct_class_padrao_pagina.cor_fundo_pagina(self.pageinit)
        self.ct_class_padrao_pagina.tamanho_tela(self.pageinit) 
        self.ct_class_padrao_pagina.titulo_pagina(self.pageinit)

    def __pagina_init(self):

        self.ct_class_index = Index()
        self.ct_class_index.sistema()

    
def main(page: Page) -> None:

    AppMain(page)


if __name__ == "__main__":
    run(main)
