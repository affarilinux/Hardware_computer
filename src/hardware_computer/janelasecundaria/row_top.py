from flet import Column, Row, MainAxisAlignment, CrossAxisAlignment, Container

#janelasecundaria.ui
from janelasecundaria.ui.drop import Drop
from janelasecundaria.ui.buttom_grafico import ButtonGrafico
from janelasecundaria.ui.configuracoes.coluna_configuracoes import (
    ColunaConfiguracoes,
)
from core.ultils.pag import Pagina


class RowTop:

    def __init__(self) -> None:

          self.j_class_button = ButtonGrafico()
          self.j_class_drop = Drop(on_select=self._atualizar_opcao)
          self.j_class_configuracoes = ColunaConfiguracoes()
          self.j_class_configuracoes.get_widget().visible = False

          self.row_dropdown()
        

    def row_dropdown(self):
    
            self.row = Column(
                expand=True,
                horizontal_alignment=CrossAxisAlignment.STRETCH,
                controls=[
                    Row(
                        width=480,
                        controls=[
                            Container(
                                content=self.j_class_button.get_iconbuton(),
                                width=48,
                            ),
                            self.j_class_drop.get_dropdown()
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.j_class_button.get_grafico(),
                    self.j_class_configuracoes.get_widget(),
                ],
                spacing=8,
            )
    
    def get_row(self):
        return self.row

    def _atualizar_opcao(self, opcao):
        # A opção Configurações ocupa a tela sem o botão de exibir gráfico.
        self.j_class_button.get_iconbuton().visible = opcao != "Configurações"
        self.j_class_button.get_grafico().visible = False
        self.j_class_configuracoes.get_widget().visible = opcao == "Configurações"
        pagina = Pagina.getpag()
        if pagina is not None:
            pagina.update()
