from flet import Row, Text, FontWeight, MainAxisAlignment

# mainwindows.core
from mainwindows.core.cores import Cores


class ConfigRam:

    SIZE = 11
    WEIGHT = FontWeight.W_500

    def fc_size(self):
        return self.SIZE

    def fc_weight(self):
        return self.WEIGHT


class UsoRam(ConfigRam):

    _instancia = None

    def __init__(self):

        self.mw_class_cores = Cores()
        self.wdg_text_total = Text(

            size=self.fc_size(),
            weight=self.fc_weight(),
            color=self.mw_class_cores.get_cor_branca(),
        )
        UsoRam._instancia = self

    @classmethod
    def get_instancia(cls):
        return cls._instancia

    def top_Row(self):
        return Row(
            controls=[self.wdg_text_total],
            width=170,
            alignment=MainAxisAlignment.CENTER,
        )

    def atualizar_total_ram(self, usada_bytes, total_bytes):
        usada_gb = usada_bytes / (1024 ** 3)
        total_gb = total_bytes / (1024 ** 3)
        self.wdg_text_total.value = (
            f"{usada_gb:.1f} GB usados / {total_gb:.1f} GB total"
        )
