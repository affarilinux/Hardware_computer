from flet import Column, CrossAxisAlignment

# mainwindows.ui
from mainwindows.ui.front_statics import FrontStatics
from mainwindows.ui.memoria_ram.stack_ram import StackRam


class Coluna:

    def __init__(self):

        self.wdg_coluna = Column(
            width=170,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0,
        )
        self.mn_class_front_statics = FrontStatics()
        self.ct_class_stack_ram = StackRam()

    def controls_column_adicionar(self, controls):

        self.wdg_coluna.controls.append(

            controls,

        )


class GrupoRamColuna(Coluna):

    def __init__(self):
        super().__init__()

        self.__adicionar_controls()

    def __adicionar_controls(self):

        # função esterna
        self.controls_column_adicionar(
            self.ct_class_stack_ram.get_stack()
        )

        self.controls_column_adicionar(
            self.mn_class_front_statics.text_memoria_ram()
        )

        self.controls_column_adicionar(
            self.mn_class_front_statics.divider()
        )

    def get_widget_grupo_coluna(self):

        # class coluna
        return self.wdg_coluna
