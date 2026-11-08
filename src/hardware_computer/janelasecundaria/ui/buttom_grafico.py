from flet import IconButton, Icons

from janelasecundaria.ui.grafico import Grafico
from core.ultils.pag import Pagina


class widgetButtom:

    def __init__(self) -> None:

        self.ju_class_grafico = Grafico()
        self.icon_button()

    def icon_button(self):

        self.wdg_button = IconButton(
            icon=Icons.SSID_CHART_SHARP,
            tooltip="Mostrar gráfico",
            on_click=self.alternar_grafico,
        )

    def alternar_grafico(self, _evento=None):
        grafico = self.ju_class_grafico.get_grafico()
        grafico.visible = not grafico.visible
        self.wdg_button.icon = Icons.CLOSE if grafico.visible else Icons.SSID_CHART_SHARP
        self.wdg_button.tooltip = (
            "Ocultar gráfico" if grafico.visible else "Mostrar gráfico"
        )

        pagina = Pagina.getpag()
        if pagina is not None:
            pagina.update()


class ButtonGrafico(widgetButtom):

    def get_iconbuton(self):
        return self.wdg_button

    def get_grafico(self):
        return self.ju_class_grafico.get_grafico()

