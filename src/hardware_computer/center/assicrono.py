
# core
from core.ultils.pag import Pagina

# backend correspondente
# Ajuste o import conforme sua estrutura de pastas
from center.back_assicrono import BackAssincrono


class Assicrono:

    def __init__(self) -> None:
        self.backend = BackAssincrono()

    def sistema_assincrono(self):
        self.__ativar_loop()

    def __ativar_loop(self):
        # Passa a função assíncrona diretamente para o run_task do Flet
        Pagina.getpag().run_task(self.backend.iniciar_loop_background)
