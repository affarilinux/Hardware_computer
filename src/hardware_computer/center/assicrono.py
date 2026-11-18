
# core
from core.ultils.pag import Pagina

# backend correspondente
# Ajuste o import conforme sua estrutura de pastas
from center.back_assicrono import BackAssincrono


class Assicrono:

    # O aplicativo usa uma página global (Pagina). Reutilize o backend e
    # inicie apenas uma tarefa para evitar contagens duplicadas.
    _backend_compartilhado = None
    _loop_iniciado = False

    def __init__(self) -> None:
        if Assicrono._backend_compartilhado is None:
            Assicrono._backend_compartilhado = BackAssincrono()
        self.class_ba = Assicrono._backend_compartilhado

    def sistema_assincrono(self):

        self.__ativar_loop()

    def __ativar_loop(self):
        pagina = Pagina.getpag()
        if pagina is not None and not Assicrono._loop_iniciado:
            pagina.run_task(self.class_ba.iniciar_loop_background)
            Assicrono._loop_iniciado = True
