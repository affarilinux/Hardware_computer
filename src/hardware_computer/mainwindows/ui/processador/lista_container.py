from flet import Container,Alignment,Stack,Colors

# ui.processador
from mainwindows.ui.processador.stack import StackProcessador
from mainwindows.ui.processador.grid import GridProcessador


class WidgetContainer:

    def __init__(self):
        
        self.wdg_container = Container()

        #funcao interna
        self.ativar_funcoes()

    def ativar_funcoes(self):

        self.__tamanho_container()

        self.__borda_radius()

        self.__alignment()

        #self.__cor_fundo_container()
    
    def __tamanho_container(self):
        #largura
        self.wdg_container.width = 170
        #altura
        self.wdg_container.height = 150

    def __borda_radius(self):
        self.wdg_container.border_radius = 10

    def __alignment(self):
        self.wdg_container.alignment = Alignment.CENTER

    '''def __cor_fundo_container(self):
        self.wdg_container.bgcolor = Colors.SURFACE_CONTAINER_HIGHEST'''

    def content(self,stack,grid):
        self.wdg_container.content = Stack(
            controls=[
                stack,
                grid,
            ],
            alignment=Alignment.CENTER,
        )

    

class ListaContainer(WidgetContainer):

    def __init__(self):

        #funcao construtora da classe pai
        super().__init__()

        
        # widget
        self.mw_class_stack_pc = StackProcessador()
        self.mw_class_gridprocessador = GridProcessador()

        #definir o content
        self.content(
            self.mw_class_stack_pc.get_stack(),
            self.mw_class_gridprocessador.get_grid(),
        )

    
    
    def get_widget_container(self):
        # class container
        return self.wdg_container

    def get_stack(self):
        
        return self.mw_class_stack_pc.get_stack()

    def get_grid(self):
        
        return self.mw_class_gridprocessador.get_grid()