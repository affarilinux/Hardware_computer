from flet import Column

from janelasecundaria.ui.configuracoes.temporizador_ciclos import (
    TemporizadorCiclos,
)


class ColunaConfiguracoes:
    def __init__(self):

        self.temporizador = TemporizadorCiclos()

        self.widget = Column(controls=[self.temporizador.get_row()])

    def get_widget(self):
        return self.widget
