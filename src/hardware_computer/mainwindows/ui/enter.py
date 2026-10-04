from flet import Column,Row,Container,MainAxisAlignment

# core 
from mainwindows.core.atividade_pagina import AtividadePagina

# ui.widgets
from mainwindows.ui.front_statics import FrontStatics

# ui.processador
from mainwindows.ui.processador.area_conteudo import AreaConteudo
from mainwindows.ui.processador.alternador import Alternador


class FrontEnter:
    num = 0

    def __init__(self):

        self.VAR_AREA_CONTEUDO = AreaConteudo()
        self.VAR_ALTER = Alternador()
        self.VAR_UISTATICS = FrontStatics()

    def front_enter(self):

        if FrontEnter.num == 0:
            FrontEnter.num = 1
            self.__ordem_execucao_components()
            

    def __ordem_execucao_components(self):
       
        self.VAR_ALTER.widget_button_alternador()
        self.VAR_AREA_CONTEUDO.area_conteudo_processador()
        self.VAR_AREA_CONTEUDO.widget_container_stack_grid()

        #stack with grid
        self.VAR_ALTER.widget_stack_grid(
            self.VAR_AREA_CONTEUDO.get_stack(),
            self.VAR_AREA_CONTEUDO.get_grid()
        )
        
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
                #processador
                Row(
                    controls=[
                        self.VAR_UISTATICS.text_processador()
                    ],
                    alignment="center_right",
                ),            
                

                #button alternador
                Row(
                    controls=[
                        self.VAR_ALTER.Get_button_alternador()
                        
                    ],
                    alignment=MainAxisAlignment.END
                ),           
                

                # % total
                Row(
                    controls=[
                        self.VAR_AREA_CONTEUDO.get_conteudo_principal()
                    ],
                    alignment="center",
                ),

            ]
        )
        return var_coluna_processador
            

                
    
                