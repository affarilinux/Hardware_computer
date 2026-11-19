import asyncio

# sistemas
from sistemas.exe_processador import ExeProcessador
from sistemas.exe_ram import ExeRam
# conjunto de classes
from sistemas.exe_temperatura import ExeTemperatura


# mainwindows
from mainwindows.front_enter import FrontEnter
from mainwindows.ui.data.data_app import DataApp

# externo
from externo.ex_bateria import ExBateria
from janelasecundaria.ui.configuracoes.temporizador_ciclos import (
    TemporizadorCiclos
)


class BackAssincrono:

    # Protege também contra chamadas diretas ou repetidas do método de loop.
    _loop_ativo = False

    def __init__(self) -> None:
        self.count = 0
        self.sys_class_exe_processador = ExeProcessador()
        self.sys_class_exe_ram = ExeRam()
        self.sys_class_exe_temperatura = ExeTemperatura()
        self.front_enter = FrontEnter()
        self.sys_class_bateria = ExBateria()

    async def iniciar_loop_background(self):
        """Loop principal executado em segundo plano a cada 1 segundo."""
        if BackAssincrono._loop_ativo:
            return

        BackAssincrono._loop_ativo = True
        try:
            while True:

                if self.count == 0:

                    # dir externo
                    self.__externo()
                    self.__sistema_front()

                    # mainwindows entrada  dados
                    self.front_enter.executar_grupo_funcao()

                DataApp.atualizar_instancia()

                self.__count_ciclos()
                await asyncio.sleep(1)
        finally:
            BackAssincrono._loop_ativo = False

    def __count_ciclos(self):
        """Gerencia a contagem de ciclos para determinar quando executar ações."""
        self.count += 1
        intervalo = TemporizadorCiclos.obter_intervalo_segundos()

        if self.count >= intervalo:
            self.count = 0
    # ---------------------------
        # estrutura esterna
    # ----------------------------

    def __externo(self):

        self.sys_class_bateria.exec_bateria()

    def __sistema_front(self):

        self.sys_class_exe_processador.exe_loop()
        self.sys_class_exe_ram.exe_loop()
        self.sys_class_exe_temperatura.exe_loop()
