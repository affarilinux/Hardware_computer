from flet import Text, FontWeight

from mainwindows.core.cores import Cores

class FrontStatics:

    def __init__(self):
        self.cores = Cores()

    def text_processador(self):
        
        return Text(
            "PROCESSADOR", 
            size=25, 
            weight=FontWeight.W_600,
            color=self.cores.get_cor_branca(),
            
            )
        