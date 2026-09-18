from flet import Column,Row,Container

# core 
from mainwindows.core.atividade_pagina import AtividadePagina

# ui.widgets
from mainwindows.ui.widgets.front_statics import FrontStatics

class FrontEnter:
    num = 0

    def __init__(self):

        self.VAR_UISTATICS = FrontStatics()
        

    def front_enter(self):

        if FrontEnter.num == 0:
            FrontEnter.num = 1
            self.__ordem_execucao_components()
            

    def __ordem_execucao_components(self):

        var_direcao_inicio = Column(
            controls=[
                self.__processador()
            ]
        )
        
        # add components to page
        var_atividade_pagina = AtividadePagina()

        var_atividade_pagina.adicionar_componentes_pagina(var_direcao_inicio)

    def __processador(self):
        
        var_coluna_processador = Column(
            controls=[

                Container(height=30),

                Row(
                    controls=[
                        self.VAR_UISTATICS.text_processador()
                    ]
                ),










                #fixo
                #self.VAR_UISTATICS.text_processador()
            ]
        )
        return var_coluna_processador
            
        