from flet import Column

#mainwindows.ui.processador
from mainwindows.ui.processador.lista_container import ListaContainer
from mainwindows.ui.processador.alternador import Alternador

class Coluna:

    def __init__(self):

        self.wdg_coluna = Column()
    
    def controls_column_adicionar(self,controls):
        
        self.wdg_coluna.controls.append(

           controls,

        )
    
class GrupoColuna(Coluna):

    def __init__(self):
        super().__init__()

        self.ct_class_lista_container = ListaContainer()
        self.ct_class_alternador = Alternador()
        
        self.__adicionar_controls()
        self.__ativar_funcoes_grid_stack()
    
    def __adicionar_controls(self):
        
        #função esterna

        self.controls_column_adicionar(
            self.ct_class_alternador.Get_button_alternador()
        )
        
        self.controls_column_adicionar(
            self.ct_class_lista_container.get_widget_container()
        )

       

    def __ativar_funcoes_grid_stack(self):

        self.ct_class_alternador.atividade_stack_grid(
            self.ct_class_lista_container.get_stack(),
            self.ct_class_lista_container.get_grid()
        )

    def get_widget_grupo_coluna(self):

        #class coluna
        return self.wdg_coluna