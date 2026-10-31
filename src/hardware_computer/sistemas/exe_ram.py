
# externo
from externo.ram import RAM

# memoria
from memoria.ram import MemoriaRam


class ExeRam:

    def __init__(self):

        self.sys_class_exe_ram = RAM()
        self.memoria_ram = MemoriaRam()

    def exe_loop(self):
        """
        atualizacao de lista pelo loop
        """
        self.__total_memoria()
        self.__memoria_usada()
        self.__porcentagem_usada()

    def __total_memoria(self):

        __var_lista = []

        __var_status_valor = self.sys_class_exe_ram.total_memoria()

        if __var_status_valor[0] == True:

            __var_lista.append(True)
            __var_lista.append(__var_status_valor[1])

        elif __var_status_valor[0] == False:

            __var_lista.append(False)
            __var_lista.append(0)

        self.memoria_ram.set_status(__var_lista[0])
        self.memoria_ram.set_total_memoria(__var_lista[1])

    def __memoria_usada(self):

        __var_lista = []

        __var_status_valor = self.sys_class_exe_ram.memoria_usada()

        if __var_status_valor[0] == True:

            __var_lista.append(True)
            __var_lista.append(__var_status_valor[1])

        elif __var_status_valor[0] == False:

            __var_lista.append(False)
            __var_lista.append(0)

        self.memoria_ram.set_memoria_usada(__var_lista[1])

    def __porcentagem_usada(self):

        __var_total_memoria = self.memoria_ram.get_lista_ram()[
            0]["total_memoria"]
        __var_memoria_usada = self.memoria_ram.get_lista_ram()[
            0]["memoria_usada"]

        if __var_total_memoria > 0:
            porcentagem = (__var_memoria_usada / __var_total_memoria) * 100
            self.memoria_ram.set_porcentagem(porcentagem)
        else:
            self.memoria_ram.set_porcentagem(0)

        
