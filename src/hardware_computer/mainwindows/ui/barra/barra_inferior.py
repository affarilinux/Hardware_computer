from flet import (
    Alignment, BottomAppBar, CrossAxisAlignment, IconButton, Icons,
    MainAxisAlignment, Row, Container,
)

from core.ultils.pag import Pagina


class BarraInferior:
    """Barra inferior com alternância entre painel e gráficos."""

    def __init__(self, alternar_tela):
        self.alternar_tela = alternar_tela
        self.modo_graficos = False
        self.botao = Container(
            content=IconButton(
                icon=Icons.SETTINGS,
                tooltip="Abrir gráficos",
                icon_color="#FFFFFF",
                on_click=self._alternar,
            ),
            width=48, height=48, bgcolor="#303840", border_radius=24,
            alignment=Alignment.CENTER,
        )
        self.barra = BottomAppBar(
            height=56, bgcolor="#1B1B1B",
            content=Row(
                controls=[Container(expand=True), self.botao],
                alignment=MainAxisAlignment.END,
                vertical_alignment=CrossAxisAlignment.CENTER,
            ),
        )

    def instalar(self):
        pagina = Pagina.getpag()
        if pagina is not None:
            pagina.bottom_appbar = self.barra

    def _alternar(self, _evento):
        self.alternar_tela()

    def atualizar_icone(self, modo_graficos):
        self.modo_graficos = modo_graficos
        self.botao.content.icon = Icons.ARROW_BACK if modo_graficos else Icons.SETTINGS
        self.botao.content.tooltip = "Voltar ao painel" if modo_graficos else "Abrir Informações"
