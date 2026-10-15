from flet import GridView,Container,Colors,Alignment,Text


class WidgetGrid:

    def __init__(self):
        self.wdg_gridview = GridView()

        self.ativar_funcoes()

    def ativar_funcoes(self):

        self.__contagem()
        self.__espacos()
        self.__dimensao()
        self.__visible()
    
    def __contagem(self):

        self.wdg_gridview.runs_count = 3
        self.wdg_gridview.run_spacing = 10
        
    def __espacos(self):

        self.wdg_gridview.spacing = 10

    def __dimensao(self):

        self.wdg_gridview.width = 160
        self.wdg_gridview.height = 190

    def __visible(self):

        self.wdg_gridview.visible = False

    def add_widget(self,numero):

        self.wdg_gridview.controls.append(
            Container(
                    content=Text(f"Widget {numero}"),
                    bgcolor=Colors.BLUE_GREY_800,
                    border_radius=10,
                    alignment=Alignment.CENTER,
                )
        )
        

class GridProcessador(WidgetGrid):

    def __init__(self):
        super().__init__()

        self.for_processadores()

    def for_processadores(self):

       
        for i in range(6):

            self.add_widget(i+1)
                
    def get_grid(self):
        return self.wdg_gridview
        