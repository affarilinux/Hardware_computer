from flet import Column, Container, CrossAxisAlignment

# mainwindows.ui

from mainwindows.ui.temperatura.cpu_temp import CpuTemp
from mainwindows.ui.temperatura.linha_1 import Linha1
from mainwindows.ui.temperatura.linha_2 import Linha2


class Coluna:

    def __init__(self):

        self.wdg_coluna = Column(
            width=170,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0,
        )

        self.mw_class_cputemp = CpuTemp()
        self.mw_class_linha1 = Linha1()
        self.mw_class_linha2 = Linha2()

    def controls_column_adicionar(self, controls):

        self.wdg_coluna.controls.append(

            controls,

        )


class GrupoTempColuna(Coluna):

    def __init__(self):
        super().__init__()

        self.__adicionar_controls()

    def __adicionar_controls(self):

        # função esterna

        self.controls_column_adicionar(
            self.mw_class_cputemp.Coluna_cpu()

        )
        # Compensa a altura menor da linha de uso da RAM em relação ao botão
        # de alternância do processador, alinhando os dois gráficos e divisores.
        self.controls_column_adicionar(Container(height=10))

        self.controls_column_adicionar(
            self.mw_class_linha1.Row_linha_1()
        )
        self.controls_column_adicionar(Container(height=10))

        self.controls_column_adicionar(
            self.mw_class_linha2.Row_linha_2()
        )

    def get_widget_grupo_coluna(self):

        # class coluna
        return self.wdg_coluna
