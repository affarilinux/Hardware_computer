import psutil

from memoria.mem_bateria import MemoriaBateria
class ExBateria:
    """Le a bateria do sistema usando ``psutil``."""

    def __init__(self) -> None:

        self.bateria = None
        self.E_class_memoriabateria = MemoriaBateria()

        

    
    def exec_bateria(self):

        self.__psutil_bateria()
        self.__obter_bateria()
        self.__plugue_energia()
        self.__atualizar_memoria()

    def __psutil_bateria(self):

        self.bateria = psutil.sensors_battery()

    def __obter_bateria(self):
        """Obtém informações da bateria porcentagem."""

        self.__lista_bateria = []
        if self.bateria:
            
            self.__lista_bateria = [True, self.bateria.percent]
        else:
            self.__lista_bateria = [False, 0]


    def __plugue_energia(self):
        """Verifica se o sistema está conectado à energia."""

        self.__lista_carga = []

        if self.bateria:
            self.__lista_carga = [True, self.bateria.power_plugged]
        else:
            self.__lista_carga = [False, False]

    def __atualizar_memoria(self):

        self.E_class_memoriabateria.set_status_bateria(self.__lista_bateria[0])
        self.E_class_memoriabateria.set_porcentagem(self.__lista_bateria[1])
        self.E_class_memoriabateria.set_carregando(self.__lista_carga[1])