from flet import Column, CrossAxisAlignment, Container, Stack, Alignment

# mainwindows.ui
from mainwindows.ui.bateria.stack_batery import StackBateria
from mainwindows.ui.bateria.botao_batery import BotaoBateria
from mainwindows.ui.front_statics import FrontStatics


class Coluna:

    def __init__(self):

        self.wdg_coluna = Column(
            width=170,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0,
        )

        self.mw_class_frontstatics = FrontStatics()
        self.mw_class_stackbateria = StackBateria()
        self.mw_class_botaobateria = BotaoBateria()

    def controls_column_adicionar(self, controls):

        self.wdg_coluna.controls.append(

            controls,

        )


class GrupoBateria(Coluna):

    def __init__(self):
        super().__init__()

        self.__adicionar_controls()

    def __adicionar_controls(self):

        # função esterna
        self.controls_column_adicionar(
            self.mw_class_stackbateria.get_stack()
        )
        self.controls_column_adicionar(
            Stack(
                width=150,
                height=20,
                controls=[
                    Container(
                        content=self.mw_class_frontstatics.Text_bateria(),
                        width=150,
                        height=20,
                        alignment=Alignment.CENTER,
                    ),
                    Container(
                        content=self.mw_class_botaobateria.get_botao(),
                        width=150,
                        height=20,
                        alignment=Alignment.CENTER_RIGHT,
                    ),
                ],
            )
        )

        self.controls_column_adicionar(
            self.mw_class_frontstatics.divider()

        )

    def get_widget_grupo_coluna(self):

        # class coluna
        return self.wdg_coluna
