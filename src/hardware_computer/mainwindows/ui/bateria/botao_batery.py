import flet as ft


class BotaoBateria:
    """Indicador circular de carregamento da bateria."""

    _instancia = None

    COR_DESCARREGANDO = "#F44336"
    CORES_CARREGANDO = ("#2196F3", "#4CAF50")

    def __init__(self):
        self.carregando = False
        self._indice_cor = 0
        self.wdg_botao = ft.Container(
            width=12,
            height=12,
            bgcolor=self.COR_DESCARREGANDO,
            border_radius=6,
        )
        BotaoBateria._instancia = self

    @classmethod
    def get_instancia(cls):
        return cls._instancia

    def get_botao(self):
        return self.wdg_botao

    def set_carregando(self, carregando: bool):
        self.carregando = bool(carregando)
        if self.carregando:
            self.wdg_botao.bgcolor = self.CORES_CARREGANDO[self._indice_cor]
            self._indice_cor = 1 - self._indice_cor
        else:
            self._indice_cor = 0
            self.wdg_botao.bgcolor = self.COR_DESCARREGANDO
