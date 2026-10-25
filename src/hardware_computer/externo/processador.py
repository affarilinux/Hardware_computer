import psutil

class ExternoProcessador:

    def get_porcentagem_cpu(self):

        __var_porcetagem = ""

        try:

            total = psutil.cpu_percent(interval=1)
            __var_porcetagem = [True,total]

        except Exception as e:
            
            __var_porcetagem = [False,e]

        return __var_porcetagem

    def get_uso_por_nucleo(self):

        __var_uso_por_nucleo = ""

        try:

            uso_por_nucleo = psutil.cpu_percent(interval=1, percpu=True)
            __var_uso_por_nucleo = [True,uso_por_nucleo]

        except Exception as e:
            
            __var_uso_por_nucleo = [False,e]

        return __var_uso_por_nucleo
            