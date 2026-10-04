from flet import Container
import flet as ft

# ui.processador
from mainwindows.ui.processador.stack import StackProcessador
from mainwindows.ui.processador.grid import GridProcessador

class AreaConteudo:

    def __init__(self):
        self.stack_processador = StackProcessador()
        self.grid_processador = GridProcessador()

    def area_conteudo_processador(self):
        

        self.stack_processador.widget_processador_widget()
        self.grid_processador.widgets_grid_processador()

    def widget_container_stack_grid(self):
        
        self.conteudo_principal  = ft.Container(

        width=170,#largura
        height=150,#altura

        #bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        border_radius=10,
        alignment=ft.Alignment.CENTER,
        content=ft.Stack(
            controls=[
                self.stack_processador.get_stack(),
                self.grid_processador.get_grid(),
            ],
            alignment=ft.Alignment.CENTER,
        ),
    )

    def get_stack(self):
        return self.stack_processador.get_stack()
    
    def get_grid(self):
        return self.grid_processador.get_grid()

    def get_conteudo_principal(self):
        return self.conteudo_principal
        