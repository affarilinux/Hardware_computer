from flet import Text, FontWeight, Divider, Container, Row


from mainwindows.core.cores import Cores


class ConfigStatics:

    FW_X = FontWeight.W_500
    SIZE = 10

    def peso_fonte(self):
        return self.FW_X

    def fc_size(self):
        return self.SIZE


class FrontStatics(ConfigStatics):

    def __init__(self):
        self.mw_class_cores = Cores()

    def text_processador(self):

        proc = Text(
            "PROCESSADOR",
            # tamanho da fonte
            size=self.fc_size(),
            # peso da fonte
            weight=self.peso_fonte(),
            color=self.mw_class_cores.get_cor_branca(),

        )

        row = Row(
            controls=[proc],
            alignment="center",
        )

        return row

    def text_memoria_ram(self):

        return Text(
            "MEMÓRIA RAM",
            # tamanho da fonte
            size=self.fc_size(),
            # peso da fonte
            weight=self.peso_fonte(),
            color=self.mw_class_cores.get_cor_branca(),

        )

    def divider(self):

        return Container(
            width=150,
            content=Divider(
                height=25,
                color=self.mw_class_cores.get_cor_branca(),
            ))
