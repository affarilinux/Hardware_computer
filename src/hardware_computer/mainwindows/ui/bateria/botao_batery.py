from flet import Icon,Icons,Container,Alignment
from core.ultils.pag import Pagina


class BotaoBateria:
    """Ícone da bateria que indica carga e estado de carregamento."""

    _instancia = None

    COR_DESCARREGANDO = "#F44336"
    CORES_CARREGANDO = ("#2196F3", "#4CAF50")

    def __init__(self):
        self.carregando = False
        self._indice_cor = 0
        self.wdg_botao = Container(
            content=Icon(
                icon=Icons.BATTERY_0_BAR,
                size=24,
                color=self.COR_DESCARREGANDO,
            ),
            width=30,
            height=30,
            alignment=Alignment.CENTER,
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
            cor = self.CORES_CARREGANDO[self._indice_cor]
            self._indice_cor = 1 - self._indice_cor
            self.wdg_botao.content.icon = Icons.BATTERY_CHARGING_FULL
            self.wdg_botao.content.color = cor
        else:
            self._indice_cor = 0
            self.wdg_botao.content.icon = Icons.BATTERY_0_BAR
            self.wdg_botao.content.color = self.COR_DESCARREGANDO

        pagina = Pagina.getpag()
        if pagina is not None:
            pagina.update()
