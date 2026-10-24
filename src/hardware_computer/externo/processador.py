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
            
            