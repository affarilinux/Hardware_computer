import psutil


class RAM:

    def __init__(self) -> None:

        self.memoria = psutil.virtual_memory()

    def total_memoria(self):

        __var_total_memoria = ""

        try:

            total_memoria = self.memoria.total
            __var_total_memoria = [True, total_memoria]

        except Exception as e:

            __var_total_memoria = [False, e]

        return __var_total_memoria

    def memoria_usada(self):

        __var_memoria_usada = ""

        try:

            memoria_usada = self.memoria.used
            __var_memoria_usada = [True, memoria_usada]

        except Exception as e:

            __var_memoria_usada = [False, e]

        return __var_memoria_usada
