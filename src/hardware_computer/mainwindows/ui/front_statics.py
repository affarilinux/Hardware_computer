from flet import Text, FontWeight

from mainwindows.core.mw_class_cores import mw_class_cores

class FrontStatics:

    def __init__(self):
        self.mw_class_cores = mw_class_cores()

    def text_processador(self):
        
        return Text(
            "PROCESSADOR", 
            size=25, 
            weight=FontWeight.W_600,
            color=self.mw_class_cores.get_cor_branca(),
            
            )
        