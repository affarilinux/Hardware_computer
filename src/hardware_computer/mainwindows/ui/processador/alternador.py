from flet import IconButton,Icons
import flet as ft

# core.ultils
from core.ultils.pag import Pagina

class Alternador:

    def widget_stack_grid(self, stack, grid):
       
        self.stack = stack
        self.grid = grid
        

    def widget_button_alternador(self):
        

        self.button_alternador = IconButton(
        icon=Icons.SWAP_HORIZ,
        tooltip="Alternar Visualização",
        on_click=self.alternar_visao,
    )

         
    
    def Get_button_alternador(self):
        
        return self.button_alternador

    
    def alternar_visao(self, e):
        # Inverte o estado de visibilidade de ambos os componentes
        self.stack.visible = not self.stack.visible
        self.grid.visible = not self.grid.visible
        Pagina.getpag().update()
    