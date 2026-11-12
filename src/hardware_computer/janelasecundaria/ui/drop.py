
from flet import Dropdown, DropdownOption


class Whidget:

    def __init__(self, on_select=None) -> None:
        self.lista = ["RAM", "Bateria", "Processador", "CPU","Configurações"]
        self.on_select = on_select

        self.widget_dropdown()

    def widget_dropdown(self):
        self.dropdown = Dropdown(
            # nome ao parecer inicial do dropdown
            label="Selecione um item:",
            # lista de opções do dropdown
            options=[DropdownOption(key=item, text=item)
                     for item in self.lista],
            width=240,
            # descrição do dropdown
            value="RAM",
            on_select=self._selecionar,
        )

    def _selecionar(self, evento):
        if self.on_select is not None:
            self.on_select(evento.control.value)


class Drop(Whidget):

    def __init__(self, on_select=None) -> None:
        super().__init__(on_select=on_select)

    def get_dropdown(self):
        return self.dropdown
