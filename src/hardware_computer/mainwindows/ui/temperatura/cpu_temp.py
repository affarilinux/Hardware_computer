from flet import Text, FontWeight, Column, Row, MainAxisAlignment

from mainwindows.core.cores import Cores


class CpuTemp:
    _instancia = None

    def __init__(self):

        self.cores = Cores()
        CpuTemp._instancia = self

    @classmethod
    def get_instancia(cls):
        return cls._instancia

    def Coluna_cpu(self):
        return Column(
            controls=[
                self.__wdg_cpu_temperatura_statics(),
                self.__temperatura()
            ]
        )

    def __wdg_cpu_temperatura_statics(self):

        return Text(
            value="CPU Temperatura",
            # tamanho da fonte
            size=20,
            weight=FontWeight.W_500,
            color=self.cores.get_cor_branca()
        )

    def __temperatura(self):

        self.var_wdg_temp = Text(


            size=25,
            weight=FontWeight.W_900,
            color=self.cores.get_cor_branca()
        )

        return Row(
            controls=[
                self.var_wdg_temp
            ],
            width=170,
            alignment=MainAxisAlignment.CENTER,

        )

    def set_cpu_temperatura_media(self, temperatura):

        self.var_wdg_temp.value = f"{temperatura} ºC"
        self.var_wdg_temp.update()
