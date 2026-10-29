from flet import Column

from mainwindows.ui.memoria_ram.grupo_ram_coluna import GrupoRamColuna


class ColunaManageresquerda:

    def __init__(self):

        self.mw_class_grupo_coluna = GrupoRamColuna()

        self.colunas()

    def colunas(self):

        self.wid_coluna = Column(
            controls=[
                self.mw_class_grupo_coluna.get_widget_grupo_coluna(),
            ]
        )

    def get_widget_coluna_direita(self):

        return self.wid_coluna
