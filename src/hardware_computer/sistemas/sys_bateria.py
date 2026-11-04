
from externo.ex_bateria import ExBateria
from memoria.mem_bateria import MemoriaBateria


class SysBateria:

    def __init__(self):
        self.ex_class_bateria = ExBateria()
        self.mm_class_bateria = MemoriaBateria()

    def exe_loop(self):
        """
        atualizacao de lista pelo loop
        """
        self.__atualizar_bateria()

    def __atualizar_bateria(self):
        # Lógica para atualizar a bateria

        lista_bateria = self.ex_class_bateria._obter_bateria()
        status_bateria = lista_bateria[0]
        porcentagem_bateria = lista_bateria[1].percent if status_bateria else 0
        carregando = lista_bateria[1].power_plugged if status_bateria else False

        self.mm_class_bateria.set_status_bateria(status_bateria)
        self.mm_class_bateria.set_porcentagem(porcentagem_bateria)
        self.mm_class_bateria.set_carregando(carregando)
