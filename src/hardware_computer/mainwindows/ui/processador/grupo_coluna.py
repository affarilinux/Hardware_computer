from flet import Column, CrossAxisAlignment

# mainwindows.ui.processador
from mainwindows.ui.processador.lista_container import ListaContainer
from mainwindows.ui.processador.alternador import Alternador
from mainwindows.ui.front_statics import FrontStatics


class Coluna:

    def __init__(self):

        self.wdg_coluna = Column(
            width=170,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0,
        )
        self.mn_class_front_statics = FrontStatics()

    def controls_column_adicionar(self, controls):

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

        # função esterna

        self.controls_column_adicionar(
            self.ct_class_alternador.Get_button_alternador()
        )

        self.controls_column_adicionar(
            self.ct_class_lista_container.get_widget_container()
        )

        self.controls_column_adicionar(
            self.mn_class_front_statics.text_processador()
        )

        self.controls_column_adicionar(
            self.mn_class_front_statics.divider()
        )

    def __ativar_funcoes_grid_stack(self):

        self.ct_class_alternador.atividade_stack_grid(
            self.ct_class_lista_container.get_stack(),
            self.ct_class_lista_container.get_grid()
        )

    def get_widget_grupo_coluna(self):

        # class coluna
        return self.wdg_coluna
