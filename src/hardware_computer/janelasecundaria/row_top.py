from flet import Column, Row, MainAxisAlignment

#janelasecundaria.ui
from janelasecundaria.ui.drop import Drop
from janelasecundaria.ui.buttom_grafico import ButtonGrafico


class RowTop:

    def __init__(self) -> None:

          self.j_class_drop = Drop()
          self.j_class_button = ButtonGrafico()

          self.row_dropdown()
        

    def row_dropdown(self):
    
            self.row = Column(
                controls=[
                    Row(
                        controls=[
                            self.j_class_button.get_iconbuton(),
                            self.j_class_drop.get_dropdown()
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    ),
                    self.j_class_button.get_grafico(),
                ],
                spacing=8,
            )
    
    def get_row(self):
        return self.row
