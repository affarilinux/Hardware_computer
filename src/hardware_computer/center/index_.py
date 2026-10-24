
from mainwindows.manager import Manager
from center.assicrono import Assicrono

class Index:

    def __init__(self):

        
        #mainwindows
        self.ct_class_manager = Manager()
        #center
        self.ct_class_assicrono = Assicrono()
    
        
    def sistema(self):    
        
        self.ct_class_manager.gerenciar_pagina()
        self.ct_class_assicrono.sistema_assincrono()
       