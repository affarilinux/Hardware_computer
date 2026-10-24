
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
