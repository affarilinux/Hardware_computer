#programas.sys_processador
from programas.sys_processador.Get_processador import Get_processador


#mainwindows
from mainwindows.front_enter import FrontEnter



class ExeProcessador:

    porcentagem = {
        "status":False,
        "porcentagem":0
    }


    def __init__(self):

        var_get_porcentagem = GetProcessador()

        

    
    def porcentagem(self,porc):

        
        var_porcentagem = porc.get_porcentagem()

        if var_porcentagem == False:

            self.porcentagem = {
                "status":False,
                "porcentagem":0
            }

        elif var_porcentagem != False:
            
            self.porcentagem = {
                "status":True,
                "porcentagem":var_porcentagem
            }

    def exe_porcentagem_processador(self):
        
        if self.porcentagem["status"] == True:

            FrontEnter.set_porcentagem_cpu(self.porcentagem["porcentagem"])
        

    
        
        

        