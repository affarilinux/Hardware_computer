
from flet import MainAxisAlignment, IconButton, Icons, Row

# core.ultils
from core.ultils.pag import Pagina


class Widgetalternador:

  def __init__(self):

    self.wdg_iconbutton = IconButton()

    self.__icone()
    self.__configurar_clique()  # Evita sobrescrever o método com o mesmo nome do evento

  def __icone(self):
    self.wdg_iconbutton.icon = Icons.SWAP_HORIZ
    self.wdg_iconbutton.tooltip = "Alternar Visualização"

  def __configurar_clique(self):
    # O evento do botão vai chamar o método da classe filha (Alternador)
    self.wdg_iconbutton.on_click = self.ao_clicar_botao


class WidgetRow:

  def __init__(self):
    self.wdg_row = Row()

  def add_wdg_row(self,controls):
    self.wdg_row.controls.append(controls)

  def alinhamento(self):
    self.wdg_row.alignment = MainAxisAlignment.END


class Alternador(Widgetalternador, WidgetRow):
  var_tipo: str = "stack"  # Corrigido para usar a variável correta

  def __init__(self):
    # CORREÇÃO: Inicializa explicitamente as duas classes pai para criar self.wdg_row e self.wdg_iconbutton
    Widgetalternador.__init__(self)
    WidgetRow.__init__(self)

    # Posiciona o botão dentro da Row logo na inicialização
    self.add_wdg_row(self.wdg_iconbutton)
    self.alinhamento()

  def atividade_stack_grid(self, Stack, Grid):
    self.stack = Stack
    self.grid = Grid

  def Get_button_alternador(self):
    return self.wdg_row

  def ao_clicar_botao(self, e):
    self.alternar_visao()
    self.alterar_tipo()

  def alternar_visao(self):
    # Inverte o estado de visibilidade de ambos os componentes
    self.stack.visible = not self.stack.visible
    self.grid.visible = not self.grid.visible

    Pagina.getpag().update()

  def alterar_tipo(self):
    if self.var_tipo == "stack":
      self.var_tipo = "grid"
    elif self.var_tipo == "grid":
      self.var_tipo = "stack"

  def get_tipo(self):
    return self.var_tipo