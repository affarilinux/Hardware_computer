from flet import Column

from janelasecundaria.drop import Drop


class ManagerJS:

    def __init__(self) -> None:

        self.js_class_drop = Drop()
        self._criar_coluna()

    def _criar_coluna(self):
        self.wdg_coluna = Column(
            controls=[
                self.js_class_drop.get_dropdown()
            ]
        )

    def Get_coluna(self):
        return self.wdg_coluna
