from flet import GridView,Container
import flet as ft

class GridProcessador:

    def widgets_grid_processador(self):

        self.grid = GridView(
        runs_count=3,
        spacing=10,
        run_spacing=10,
        width=160, #largura
        height=190, #altura
        visible=False,
        
    )

        for i in range(6):
            self.grid.controls.append(
                
                Container(
                    content=ft.Text(f"Widget {i + 1}"),
                    bgcolor=ft.Colors.BLUE_GREY_800,
                    border_radius=10,
                    alignment=ft.Alignment.CENTER,
                )
            )

        
    def get_grid(self):
        return self.grid
        