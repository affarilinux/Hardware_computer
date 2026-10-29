from flet import Row, MainAxisAlignment

from mainwindows.coluna_manager_direita import ColunaManagerDireita
from mainwindows.coluna_manager_esquerda import ColunaManageresquerda


class RowManager:

    def __init__(self) -> None:

        self.mw_class_coluna_manager = ColunaManagerDireita()
        self.mw_class_coluna_manager_esquerda = ColunaManageresquerda()

        self.rows()

    def rows(self):

        self.wid_row = Row(
            controls=[
                self.mw_class_coluna_manager_esquerda.get_widget_coluna_direita(),
                self.mw_class_coluna_manager.get_widget_coluna_direita()
            ],
            alignment= MainAxisAlignment.SPACE_EVENLY
        )

    def get_widget_row(self):

        return self.wid_row
