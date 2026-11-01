from flet import Row, Text, FontWeight, MainAxisAlignment

from mainwindows.core.cores import Cores


class Linha2:

    _instancia = None

    def __init__(self) -> None:

        self.cores = Cores()
        Linha2._instancia = self

    @classmethod
    def get_instancia(cls):
        return cls._instancia

    def Row_linha_2(self) -> Row:

        return Row(
            controls=[
                self.__wdg_perifericos(),

            ],
            alignment=MainAxisAlignment.CENTER
        )

    def __wdg_perifericos(self):

        self.wdg_perifericos = Text(

            size=12,
            color=self.cores.get_cor_branca(),
            weight=FontWeight.W_500,
        )

        return self.wdg_perifericos

    def set_perifericos_temperatura(self, temperatura):

        self.wdg_perifericos.value = f"PERIFÉRICOS: {temperatura} ºC"
        self.wdg_perifericos.update()
