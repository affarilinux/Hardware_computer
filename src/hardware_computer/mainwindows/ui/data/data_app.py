'''from datetime import datetime

from flet import (
    Column,
    Container,
    CrossAxisAlignment,
    MainAxisAlignment,
    Row,
    Text,
)
from core.ultils.pag import Pagina


class DataApp:
    """Cabeçalho com calendário semanal, data e relógio do sistema."""

    DIAS = ("DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB")
    MESES = (
        "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
        "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO",
    )
    _instancia = None

    def __init__(self):
        self._celulas_dia = []
        self._texto_data = Text(size=14, color="#17324D")
        self._texto_dia = Text(size=38, 
                               color="#17324D",
                               weight="bold")
        self._texto_hora = Text(size=34, 
                                color="#17324D",
                                weight="bold")

        linha_dias = Row(
            controls=self._celulas_dia,
            spacing=0,
            expand=True,
        )
        faixa_dia = Container(
            content=linha_dias,
            bgcolor="#D7E7FA",
            padding=0,
        )

        faixa_info = Container(
            content=Row(
                controls=[
                    Container(
                        content=self._texto_dia, 
                        width=80, 
                        alignment=None),
                    Container(content=self._texto_data, expand=True),
                    Container(content=self._texto_hora, width=180),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=CrossAxisAlignment.CENTER,
            ),
            bgcolor="#D7E7FA",
            padding=8,
        )

        self._widget = Container(
            content=Column(
                controls=[faixa_dia, faixa_info],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.STRETCH,
            ),
            width=500,
            bgcolor="#D7E7FA",
            padding=0,
        )

        # Atribui a instância atual à variável de classe _instancia
        DataApp._instancia = self
        self.atualizar()

    def get_widget(self):
        return self._widget

    @classmethod
    def atualizar_instancia(cls):
        if cls._instancia is not None:
            cls._instancia.atualizar()

    def atualizar(self):
        agora = datetime.now().astimezone()
        # Python: segunda-feira=0; a faixa da imagem começa no domingo.
        inicio_semana = agora.weekday() + 1
        if inicio_semana == 7:
            inicio_semana = 0

        # Cria as células uma única vez. Recriá-las a cada segundo pode deixar
        # o cliente Flet com patches apontando para controles já removidos.
        if not self._celulas_dia:
            for nome_dia in self.DIAS:
                self._celulas_dia.append(
                    Container(
                        content=Text(
                            value=nome_dia,
                            size=14,
                            text_align="center",
                        ),
                        expand=True,
                        alignment=None,
                        padding=8,
                    )
                )

        for indice, celula in enumerate(self._celulas_dia):
            selecionado = indice == inicio_semana
            celula.bgcolor = "#B72C70" if selecionado else "#D7E7FA"
            celula.content.color = "#FFFFFF" if selecionado else "#17324D"

        self._texto_dia.value = str(agora.day)
        self._texto_data.value = (
            f"{agora.day} DE {self.MESES[agora.month - 1]} DE {agora.year}"
        )
        self._texto_hora.value = agora.strftime("%H:%M:%S")

        pagina = Pagina.getpag()
        if pagina is not None:
            pagina.update()'''


from datetime import datetime

from flet import (
    Column,
    Container,
    CrossAxisAlignment,
    MainAxisAlignment,
    Row,
    Text,
)

from core.ultils.pag import Pagina


class DataApp:
    """Cabeçalho com calendário semanal, data e relógio."""

    # Configurações
    DIAS = ("DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB")

    MESES = (
        "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL",
        "MAIO", "JUNHO", "JULHO", "AGOSTO",
        "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO",
    )

    COR_FUNDO = "#D7E7FA"
    COR_TEXTO = "#17324D"
    COR_SELECIONADO = "#B72C70"
    COR_BRANCO = "#FFFFFF"

    LARGURA = 500

    _instancia = None

    def __init__(self):
        self._celulas_dia = []

        self._criar_textos()
        self._widget = self._criar_layout()

        DataApp._instancia = self

        self.atualizar()

    # --------------------------------------------------
    # CRIAÇÃO DOS COMPONENTES
    # --------------------------------------------------

    def _criar_textos(self):
        #calendario
        self._texto_data = Text(
            size=14,
            color=self.COR_TEXTO,
        )
        #dia
        self._texto_dia = Text(
            size=38,
            color=self.COR_TEXTO,
            weight="bold",
        )
        #horas
        self._texto_hora = Text(
            size=34,
            color=self.COR_TEXTO,
            weight="bold",
        )

    # semana
    def _criar_celulas(self):
        for nome in self.DIAS:
            celula = Container(
                content=Text(
                    value=nome,
                    size=14,
                    text_align="center",
                    weight="bold",
                ),
                expand=True,
                padding=8,
            )

            self._celulas_dia.append(celula)

        return Row(
            controls=self._celulas_dia,
            spacing=0,
            expand=True,
        )

    # --------------------------------------------------
    # CONSTRUÇÃO DO LAYOUT
    # --------------------------------------------------

    def _criar_layout(self):

        faixa_dias = Container(
            content=self._criar_celulas(),
            bgcolor=self.COR_FUNDO,
            padding=0,
        )

        faixa_info = Container(
            content=Row(
                controls=[
                    Container(
                        content=self._texto_dia,
                        width=80,
                    ),
                    Container(
                        content=self._texto_data,
                        expand=True,
                    ),
                    Container(
                        content=self._texto_hora,
                        width=180,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=CrossAxisAlignment.CENTER,
            ),
            bgcolor=self.COR_FUNDO,
            padding=8,
        )

        return Container(
            content=Column(
                controls=[
                    faixa_dias,
                    faixa_info,
                ],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.STRETCH,
            ),
            width=self.LARGURA,
            bgcolor=self.COR_FUNDO,
            padding=0,
        )

    # --------------------------------------------------
    # ATUALIZAÇÃO DO CALENDÁRIO
    # --------------------------------------------------

    def _obter_dia_semana(self, agora):
        """Converte segunda=0 para domingo=0."""

        return (agora.weekday() + 1) % 7

    def _atualizar_calendario(self, dia_atual):

        for indice, celula in enumerate(self._celulas_dia):

            selecionado = indice == dia_atual

            celula.bgcolor = (
                self.COR_SELECIONADO
                if selecionado
                else self.COR_FUNDO
            )

            celula.content.color = (
                self.COR_BRANCO
                if selecionado
                else self.COR_TEXTO
            )

    # --------------------------------------------------
    # ATUALIZAÇÃO DA DATA E HORA
    # --------------------------------------------------

    def _atualizar_data(self, agora):

        self._texto_dia.value = str(agora.day)

        self._texto_data.value = (
            f"{agora.day} DE "
            f"{self.MESES[agora.month - 1]} DE "
            f"{agora.year}"
        )

        self._texto_hora.value = agora.strftime("%H:%M:%S")

    # --------------------------------------------------
    # ATUALIZAÇÃO GERAL
    # --------------------------------------------------

    def atualizar(self):

        agora = datetime.now().astimezone()

        dia_atual = self._obter_dia_semana(agora)

        self._atualizar_calendario(dia_atual)
        self._atualizar_data(agora)

        pagina = Pagina.getpag()

        if pagina is not None:
            pagina.update()

    # --------------------------------------------------
    # ACESSO AO COMPONENTE
    # --------------------------------------------------

    def get_widget(self):
        return self._widget

    @classmethod
    def atualizar_instancia(cls):

        if cls._instancia is not None:
            cls._instancia.atualizar()

