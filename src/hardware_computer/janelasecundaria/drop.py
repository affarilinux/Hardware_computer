
from flet import Dropdown, DropdownOption, Row,MainAxisAlignment


class Whidget:

    def __init__(self) -> None:
        self.lista = ["RAM", "Bateria", "Processador", "CPU"]

        self.widget_dropdown()

    def widget_dropdown(self):
        self.dropdown = Dropdown(
            #nome ao parecer inicial do dropdown
            label= self.lista[0],
            #lista de opções do dropdown
            options=[DropdownOption(key=item, text=item) for item in self.lista],
            width=240,
            #descrição do dropdown
            value="lista de configuracoes",
            # on_select=self._atualizar_grafico,
        )


class Drop(Whidget):

    def row_dropdown(self):

        self.row = Row(
            controls=[
                self.dropdown
            ],
            alignment=MainAxisAlignment.END
        )

        return self.row

    def get_dropdown(self):
        return self.row_dropdown()
