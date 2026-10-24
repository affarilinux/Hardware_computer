from flet import Text,FontWeight,Stack,ProgressRing,Container,Alignment
from dataclasses import dataclass

#mainwindows.core
from mainwindows.core.cores import Cores

#core.ultils
from core.ultils.pag import Pagina

@dataclass
class config:
    CENTO_E_TRINTA = 130
    
    width : int = CENTO_E_TRINTA
    height : int = CENTO_E_TRINTA


class StackProcessadorWidget:

    def __init__(self):

        self.WDG_STACK = Stack()

        #config
        self.MW_CLASS_DC_CONFIG = config()
        #cores
        self.cores = Cores()

        self.ativar_funcoes()


    def ativar_funcoes(self):
        self.__controls()

    def __controls(self):

        self.WDG_STACK.controls = [
            self.__progresso(),
            self.__container(),
        ]
        
    def __progresso(self):
        self.WDG_CLASS_PROGRESSRING = ProgressRing(
        value=0.75,       # 75%
        width=self.MW_CLASS_DC_CONFIG.width,
        height=self.MW_CLASS_DC_CONFIG.height,
        stroke_width=8,
        )

        return self.WDG_CLASS_PROGRESSRING

    def __container(self):
        return Container(
            content=self.__texto(),
            width=self.MW_CLASS_DC_CONFIG.width,
            height=self.MW_CLASS_DC_CONFIG.height,
            alignment=Alignment.CENTER,
        )

    def __texto(self):
        self.WDG_CLASS_TEXT = Text(
           
            weight=FontWeight.W_900, #grosura da letra
            color=self.cores.get_cor_branca(),
            size=25 # tamanho da letra
            
        )

        return self.WDG_CLASS_TEXT

    
class StackProcessador(StackProcessadorWidget):

    _instancia = None

    def __init__(self):
        super().__init__()
        # Salva a instância atual na variável global da classe
        StackProcessador._instancia = self

    @classmethod
    def get_instancia(cls):
        """
        Retorna a instância ativa de StackProcessador de qualquer lugar do sistema.
        """
        return cls._instancia
    
    def get_stack(self):
        return self.WDG_STACK

    def set_calculo(self, valor):
        

        self.WDG_CLASS_TEXT.value = str(round(valor,2)) + "%"
        Pagina.getpag().update()
       
            
