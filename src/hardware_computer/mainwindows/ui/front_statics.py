from flet import Text, FontWeight

from mainwindows.core.cores import Cores


class ConfigStatics:

    FW_X = FontWeight.W_500
    SIZE = 23

    def peso_fonte(self):
        return self.FW_X

    def fc_size(self):
        return self.SIZE


class FrontStatics(ConfigStatics):

    def __init__(self):
        self.mw_class_cores = Cores()

    def text_processador(self):

        return Text(
            "PROCESSADOR",
            # tamanho da fonte
            size=self.fc_size(),
            # peso da fonte
            weight=self.peso_fonte(),
            color=self.mw_class_cores.get_cor_branca(),

        )
