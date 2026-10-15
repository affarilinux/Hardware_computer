from externo.processador import ExternoProcessador

class AppProcessador:

    def __init__(self):

        self.var_externo_processador = ExternoProcessador()

    def App_processador(self):

        var_porcetagem = self.var_externo_processador.get_porcentagem_cpu()

        if var_porcetagem[0] == True:

            return var_porcetagem[1]
        
        elif var_porcetagem[0] == False:

            print(var_porcetagem[1])
            return False


        
        

