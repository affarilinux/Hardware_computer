from sys_processador.appprocessador import App_Processador

class GetProcessador:

    

    def __init__(self):
        self.app_processador = App_Processador()

    def get_porcentagem(self):

        var_porcentagem_if = ""

        var_if = self.app_processador.App_processador()

        if var_if == False:
            
            var_porcentagem_if = False

        elif var_if != False:
            
            var_porcentagem_if = var_if
                
        
        return var_porcentagem_if

    

        