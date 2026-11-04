from flet import Column

# core
# central da pagina
from mainwindows.core.atividade_pagina import AtividadePagina

from mainwindows.row_manager import RowManager
from mainwindows.ui.data.data_app import DataApp
from mainwindows.ui.barra.barra_inferior import BarraInferior
from core.ultils.pag import Pagina
#from janelasecundaria.tela_graficos import TelaGraficos
from janelasecundaria.manager import ManagerJS


class Manager:

    def __init__(self):

        # core - central pagina
        self.MW_class_atividade_pagina = AtividadePagina()
        # ui
        # self.MW_class_grupo_coluna = GrupoColuna()
        self.MW_class_row_manager = RowManager()
        self.MW_class_data_app = DataApp()
        self.MW_class_managerjs = ManagerJS()

    def gerenciar_pagina(self):

        self.__app_whidget()

    # ----------------------------
    # centro widgets
    # ----------------------------
    def __app_whidget(self):

        self.MW_class_barra_inferior = BarraInferior(self._alternar_tela)
        self.MW_class_barra_inferior.instalar()

        self.wdg_inicio_coluna = Column(
            controls=[
                self.MW_class_data_app.get_widget(),
                # processador
                # self.MW_class_grupo_coluna.get_widget_grupo_coluna(),
                # row
                self.MW_class_row_manager.get_widget_row(),



            ]
        )

        self.wdg_graficos = self.MW_class_managerjs.Get_coluna()
        self.wdg_inicio_coluna.visible = True
        self.wdg_graficos.visible = False

        # Mantém as duas telas montadas para que atualizações em segundo
        # plano não atinjam controles que foram removidos da página.
        self.MW_class_atividade_pagina.adicionar_componentes_pagina(
            self.wdg_inicio_coluna)
        self.MW_class_atividade_pagina.adicionar_componentes_pagina(
            self.wdg_graficos)

    def _alternar_tela(self):
        pagina = Pagina.getpag()
        if pagina is None:
            return
        self._modo_graficos = not getattr(self, "_modo_graficos", False)
        self.wdg_inicio_coluna.visible = not self._modo_graficos
        self.wdg_graficos.visible = self._modo_graficos
        self.MW_class_barra_inferior.atualizar_icone(self._modo_graficos)
        pagina.update()
