from flet import (
    Row, Column,
    Text, TextField, TextAlign,
    IconButton, Icons,
    KeyboardType
)
from janelasecundaria.db.SQLite_temporizador_ciclos import (
    SQLiteTemporizadorCiclos)

from core.ultils.pag import Pagina


class Whidgetciclos:

    def __init__(self) -> None:

        self.ju_class_db_tc = SQLiteTemporizadorCiclos()

        self.text_frase()
        self.numero()
        self.numero_db()

        self.icon_superior()
        self.icon_inferior()

    def text_frase(self):

        self.frase = Text(
            "Temporizador de ciclos: ",
            size=16
        )

    def numero(self):

        # Texto que armazena o valor numérico
        self.txt_numero = TextField(

            text_align=TextAlign.CENTER,
            width=100,
            keyboard_type=KeyboardType.NUMBER  # Abre o teclado numérico no celular
        )

    def numero_db(self):

        self.txt_numero.value = str(
            self.ju_class_db_tc.selecionar_linha_1() or 5)

    def icon_superior(self):

        self.var_icon_superior = IconButton(
            icon=Icons.ARROW_DROP_UP,
            on_click=self.alterar_valor,
            icon_size=24,
            padding=0
        )

    def icon_inferior(self):

        self.var_icon_inferior = IconButton(
            icon=Icons.ARROW_DROP_DOWN,
            on_click=self.alterar_valor,
            icon_size=24,
            padding=0
        )

    # Função para alterar o número
    def alterar_valor(self, e):

        atual = int(self.txt_numero.value)
        atualizado = ""

        if e.control.icon == Icons.ARROW_DROP_UP:

            atualizado = str(atual + 1)

        elif e.control.icon == Icons.ARROW_DROP_DOWN:

            atualizado = str(atual - 1)

        self.txt_numero.value = atualizado

        Pagina.getpag().update()

        self.ju_class_db_tc.atualizar_linha_1(atualizado)


class TemporizadorCiclos(Whidgetciclos):

    @classmethod
    def obter_intervalo_segundos(cls):
        """Lê do banco o intervalo usado pelo loop em segundo plano."""
        intervalo = SQLiteTemporizadorCiclos().selecionar_linha_1()
        try:
            return max(1, int(intervalo))
        except (TypeError, ValueError):
            return 5

    def __init__(self) -> None:
        super().__init__()

        self.__row()

    def __row(self):

        self.widget_row = Row(
            controls=[
                self.frase,
                self.txt_numero,
                self.__coluna()


            ]
        )

    def __coluna(self):

        coluna = Column(
            controls=[
                self.var_icon_superior,
                self.var_icon_inferior

            ]
        )

        return coluna

    def get_row(self):

        return self.widget_row
