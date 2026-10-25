from flet import Column

# core
# central da pagina
from mainwindows.core.atividade_pagina import AtividadePagina

# ui.processador
from mainwindows.ui.processador.grupo_coluna import GrupoColuna
from mainwindows.ui.front_statics import FrontStatics


class Manager:

    def __init__(self):

        # core - central pagina
        self.MW_class_atividade_pagina = AtividadePagina()
        # ui
        self.MW_class_grupo_coluna = GrupoColuna()
        self.MW_class_front_statics = FrontStatics()

    def gerenciar_pagina(self):

        self.__app_whidget()

    # ----------------------------
    # centro widgets
    # ----------------------------
    def __app_whidget(self):

        wdg_inicio_coluna = Column(
            controls=[
                #statics processador
                self.MW_class_front_statics.text_processador(),
                #processador
                self.MW_class_grupo_coluna.get_widget_grupo_coluna()
            ]
        )

        self.MW_class_atividade_pagina.adicionar_componentes_pagina(
            wdg_inicio_coluna)
