from flet import Row, Text, MainAxisAlignment, FontWeight

from mainwindows.core.cores import Cores


class Linha1:

    _instancia = None

    def __init__(self) -> None:

        self.cores = Cores()
        Linha1._instancia = self

    @classmethod
    def get_instancia(cls):
        return cls._instancia

    def Row_linha_1(self) -> Row:

        return Row(
            controls=[
                self.__wdg_placa_mae(),
                self.__wdg_wifi()

            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )

    def __wdg_placa_mae(self):

        self.wdg_placamae = Text(
            
            size=12,
            color=self.cores.get_cor_branca(),
            weight=FontWeight.W_500,
        )

        return self.wdg_placamae

    def __wdg_wifi(self):

        self.wdg_wifi = Text(
            
            size=12,
            color=self.cores.get_cor_branca(),
            weight=FontWeight.W_500,
        )

        return self.wdg_wifi


    def set_wifi_temperatura(self, temperatura):

        self.wdg_wifi.value = f"WIFI: {temperatura} ºC"
        self.wdg_wifi.update()

    def set_placa_mae_temperatura(self, temperatura):

        self.wdg_placamae.value = f"PLACA: {temperatura} ºC"
        self.wdg_placamae.update()
