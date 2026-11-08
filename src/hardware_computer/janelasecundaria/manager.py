from flet import Column

from janelasecundaria.row_top import RowTop


class ManagerJS:

    def __init__(self) -> None:

        self.js_class_rowtop = RowTop()
        self._criar_coluna()

    def _criar_coluna(self):
        self.wdg_coluna = Column(
            controls=[
                self.js_class_rowtop.get_row()
            ]
        )

    def Get_coluna(self):
        return self.wdg_coluna
