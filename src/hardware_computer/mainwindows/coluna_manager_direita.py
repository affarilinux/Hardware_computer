from flet import Column

from mainwindows.ui.processador.grupo_coluna import GrupoColuna
from mainwindows.ui.temperatura.grupo_temperatura import GrupoTempColuna


class ColunaManagerDireita:

    def __init__(self):

        self.mw_class_grupo_coluna = GrupoColuna()
        self.mw_class_grupo_temperatura = GrupoTempColuna()

        self.colunas()

    def colunas(self):

        self.wid_coluna = Column(
            controls=[
                self.mw_class_grupo_coluna.get_widget_grupo_coluna(),
                self.mw_class_grupo_temperatura.get_widget_grupo_coluna(),
            ]
        )

    def get_widget_coluna_direita(self):

        return self.wid_coluna
