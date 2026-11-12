import psutil

class ExternoProcessador:

    def get_porcentagem_cpu(self):

        __var_porcetagem = ""

        try:

            # interval=None usa o intervalo desde a amostra anterior e não
            # bloqueia a interface enquanto aguarda a próxima leitura.
            total = psutil.cpu_percent(interval=None)
            __var_porcetagem = [True,total]

        except Exception as e:
            
            __var_porcetagem = [False,e]

        return __var_porcetagem

    def get_uso_por_nucleo(self):

        __var_uso_por_nucleo = ""

        try:

            uso_por_nucleo = psutil.cpu_percent(interval=None, percpu=True)
            __var_uso_por_nucleo = [True,uso_por_nucleo]

        except Exception as e:
            
            __var_uso_por_nucleo = [False,e]

        return __var_uso_por_nucleo
