from flet import Text,FontWeight,Stack,ProgressRing,Container,Alignment
from dataclasses import dataclass
from mainwindows.core.cores import Cores

@dataclass
class config:
    CENTO_E_TRINTA = 130
    
    width : int = CENTO_E_TRINTA
    height : int = CENTO_E_TRINTA
    
class StackProcessador:

    def __init__(self):
        self.cores = Cores()
        self.config_class = config()
    
    def widget_processador_widget(self):
        
        self.stack = Stack(
            controls=[
                self.__progresso(),
                Container(
                    content=self.__texto(),
                    width=self.config_class.width,
                    height=self.config_class.height,
                    alignment=Alignment.CENTER,
                ),
            ]
        )
            

    def __texto(self):
        return Text(
            "100.00 %",
            weight=FontWeight.W_900, #grosura da letra
            color=self.cores.get_cor_branca(),
            size=25 # tamanho da letra
            
        )

    def __progresso(self):
        
        return ProgressRing(
        value=0.75,       # 75%
        width=self.config_class.width,
        height=self.config_class.height,
        stroke_width=8,
        )

    def get_stack(self):
        return self.stack
        