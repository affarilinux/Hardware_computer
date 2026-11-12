import sqlite3
from contextlib import contextmanager
from pathlib import Path

from flet import (
    Column,
    CrossAxisAlignment,
    IconButton,
    Icons,
    KeyboardType,
    MainAxisAlignment,
    Row,
    Text,
    TextAlign,
    TextField,
)

from core.ultils.pag import Pagina


class TemporizadorCiclos:
    """Widget para consultar, escolher e apagar o intervalo de ciclos."""

    INTERVALO_PADRAO = 10
    CAMINHO_BANCO = Path(__file__).with_name("configuracoes.sqlite3")
    _NAO_CARREGADO = object()
    _tempo_cache = _NAO_CARREGADO

    def __init__(self) -> None:
        salvo = self.ler_tempo_definido()
        valor_inicial = salvo if salvo is not None else self.INTERVALO_PADRAO

        self.texto_estado = Text(size=16)
        self.campo_tempo = TextField(
            value=str(valor_inicial),
            text_align=TextAlign.CENTER,
            width=100,
            keyboard_type=KeyboardType.NUMBER,
            on_change=self._ao_editar_tempo,
        )
        self._atualizar_texto_estado(salvo)

        self.widget = Column(
            controls=[
                Text("Temporizador de ciclos:", size=18, weight="bold"),
                self.texto_estado,
                Row(
                    controls=[
                        self.campo_tempo,
                        Column(
                            controls=[
                                self._criar_botao(Icons.ARROW_DROP_UP, "Aumentar tempo"),
                                self._criar_botao(Icons.ARROW_DROP_DOWN, "Diminuir tempo"),
                            ],
                            spacing=0,
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        IconButton(
                            icon=Icons.DELETE_OUTLINE,
                            tooltip="Apagar tempo definido",
                            on_click=self._apagar_tempo,
                        ),
                    ],
                    alignment=MainAxisAlignment.START,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=8,
        )

    @classmethod
    @contextmanager
    def _conectar_banco(cls):
        conexao = sqlite3.connect(cls.CAMINHO_BANCO)
        conexao.execute(
            "CREATE TABLE IF NOT EXISTS configuracoes ("
            "chave TEXT PRIMARY KEY, valor INTEGER NOT NULL)"
        )
        try:
            yield conexao
        finally:
            conexao.close()

    @classmethod
    def ler_tempo_definido(cls):
        with cls._conectar_banco() as conexao:
            registro = conexao.execute(
                "SELECT valor FROM configuracoes WHERE chave = ?",
                ("temporizador_ciclos_segundos",),
            ).fetchone()
        return registro[0] if registro else None

    @classmethod
    def obter_intervalo_segundos(cls):
        if cls._tempo_cache is cls._NAO_CARREGADO:
            cls._tempo_cache = cls.ler_tempo_definido()
        if cls._tempo_cache is None:
            return cls.INTERVALO_PADRAO
        return cls._tempo_cache

    @classmethod
    def salvar_tempo_definido(cls, segundos):
        segundos = max(1, int(segundos))
        with cls._conectar_banco() as conexao:
            conexao.execute(
                "INSERT INTO configuracoes (chave, valor) VALUES (?, ?) "
                "ON CONFLICT(chave) DO UPDATE SET valor = excluded.valor",
                ("temporizador_ciclos_segundos", segundos),
            )
        cls._tempo_cache = segundos

    @classmethod
    def apagar_tempo_definido(cls):
        with cls._conectar_banco() as conexao:
            conexao.execute(
                "DELETE FROM configuracoes WHERE chave = ?",
                ("temporizador_ciclos_segundos",),
            )
        cls._tempo_cache = None

    def get_widget(self):
        return self.widget

    def get_row(self):
        # Mantém compatibilidade com a chamada existente em ColunaConfiguracoes.
        return self.widget

    def _criar_botao(self, icone, descricao):
        return IconButton(
            icon=icone,
            tooltip=descricao,
            on_click=self._alterar_por_seta,
            icon_size=24,
            padding=0,
        )

    def _formatar_estado(self, segundos, padrao=False):
        if padrao:
            return f"Temporizador atual: {segundos} s (padrão)"
        return f"Tempo salvo no banco: {segundos} s"

    def _atualizar_texto_estado(self, salvo):
        if salvo is None:
            self.texto_estado.value = self._formatar_estado(
                self.INTERVALO_PADRAO, padrao=True
            )
        else:
            self.texto_estado.value = self._formatar_estado(salvo)

    def _definir_tempo(self, valor):
        try:
            segundos = int(valor)
        except (TypeError, ValueError):
            return
        if segundos < 1:
            return
        self.salvar_tempo_definido(segundos)
        self.campo_tempo.value = str(segundos)
        self._atualizar_texto_estado(segundos)
        self._atualizar_pagina()

    def _alterar_por_seta(self, evento):
        try:
            atual = int(self.campo_tempo.value or self.INTERVALO_PADRAO)
        except ValueError:
            atual = self.INTERVALO_PADRAO
        if evento.control.icon == Icons.ARROW_DROP_UP:
            atual += 1
        else:
            atual = max(1, atual - 1)
        self._definir_tempo(atual)

    def _ao_editar_tempo(self, evento):
        self._definir_tempo(evento.control.value)

    def _apagar_tempo(self, _evento=None):
        self.apagar_tempo_definido()
        self.campo_tempo.value = str(self.INTERVALO_PADRAO)
        self._atualizar_texto_estado(None)
        self._atualizar_pagina()

    @staticmethod
    def _atualizar_pagina():
        pagina = Pagina.getpag()
        if pagina is not None:
            pagina.update()
