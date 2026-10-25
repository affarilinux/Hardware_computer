
# memoria.processador
from memoria.processador import MemoriaProcessador
# externos.processador
from externo.processador import ExternoProcessador


class ExeProcessador:

    def __init__(self):

        self.sys_class_memoria_processador = MemoriaProcessador()

        self.sys_class_exe_processador = ExternoProcessador()

    def exe_loop(self):
        """
        atualizacao de lista pelo loop
        """
        self.__porcentagem_cpu()
        self.__lista_uso_por_nucleo()

    def __porcentagem_cpu(self):

        __var_lista = []

        __var_status_valor = self.sys_class_exe_processador.get_porcentagem_cpu()

        if __var_status_valor[0] == True:

            __var_lista.append(True)
            __var_lista.append(__var_status_valor[1])

        elif __var_status_valor[0] == False:

            __var_lista.append(False)
            __var_lista.append(0)

        self.sys_class_memoria_processador.set_status(__var_lista[0])
        self.sys_class_memoria_processador.set_porcentagem(__var_lista[1])

    def __lista_uso_por_nucleo(self):

        __var_lista_nucleo = []

        __var_status_valor = self.sys_class_exe_processador.get_uso_por_nucleo()

        if __var_status_valor[0] == True:

            __var_lista_nucleo.append(True)
            __var_lista_nucleo.append(__var_status_valor[1])

        elif __var_status_valor[0] == False:

            __var_lista_nucleo.append(False)
            __var_lista_nucleo.append(0)

        self.sys_class_memoria_processador.set_status_nucleo(
            __var_lista_nucleo[0])
        self.sys_class_memoria_processador.set_uso_por_nucleo(
            __var_lista_nucleo[1])
