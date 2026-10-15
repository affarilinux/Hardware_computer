import psutil

class ExternoProcessador:

    def get_porcentagem_cpu(self):

        var_porcetagem = ""

        try:

            total = psutil.cpu_percent(interval=1)
            var_porcetagem = [True,total]

        except Exception as e:
            
            var_porcetagem = [False,e]

        return var_porcetagem
            
            