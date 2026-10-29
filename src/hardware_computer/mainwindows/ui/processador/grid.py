from flet import GridView, Container, Alignment, Text,Colors

# core.ultils
from core.ultils.pag import Pagina

#mainwindows
from mainwindows.core.cores import Cores


class WidgetGrid:

    def __init__(self):
        self.wdg_gridview = GridView()
        self.cores = Cores()
        
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

    def add_widget(self, numero):
        self.wdg_gridview.controls.append(self._criar_widget(numero))
        Pagina.getpag().update()

    def _criar_widget(self, numero):
        return Container(
            content=Text(
                str(numero),
                color=self.cores.get_cor_branca(),
                ),
            bgcolor=Colors.BLUE_GREY_800,
            border_radius=10,
            alignment=Alignment.CENTER,
            
        )


class GridProcessador(WidgetGrid):

    _instancia = None

    def __init__(self):
        super().__init__()
        GridProcessador._instancia = self

    @classmethod
    def get_instancia(cls):
        return cls._instancia

    def for_processadores(self, processadores):

        controles = self.wdg_gridview.controls

        for indice, valor in enumerate(processadores):
            if indice < len(controles):
                controles[indice].content.value = str(valor)
            else:
                controles.append(self._criar_widget(valor))

        # Mantém no grid somente os controles correspondentes aos núcleos atuais.
        del controles[len(processadores):]
        Pagina.getpag().update()

    def get_grid(self):
        return self.wdg_gridview
