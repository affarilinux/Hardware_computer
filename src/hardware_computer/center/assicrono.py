import asyncio

from core.ultils.pag import Pagina

#mainwindows
from mainwindows.manager import Manager

class Assicrono:

    def __init__(self):

        #def __meu_loop()
        self.var_manager = Manager()
    
       
    def sistema_assincrono(self):

        self.__ativar_loop()
    
    # Função assíncrona para o loop em segundo plano
    async def __meu_loop(self):
        
        while True:
            
            self.var_manager.gerenciar_pagina()
           
            # Pausa assíncrona para não travar a interface
            await asyncio.sleep(1)

    # Executa a tarefa assíncrona na página

    def __ativar_loop(self):

        Pagina.getpag().run_task(self.__meu_loop)
        