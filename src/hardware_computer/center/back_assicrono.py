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

                    self.__externo()
                    self.__front_enter_janelamain()

                DataApp.atualizar_instancia()
                self._executar__processador_porcentagem()
                self._executar__uso_por_nucleo()
                self._executar_ram_porcentagem()
                self.__executar_temperatura_wifi()

                self.__count_ciclos()
                await asyncio.sleep(1)
        finally:
            BackAssincrono._loop_ativo = False

    def _executar__processador_porcentagem(self):
        """Gerencia a contagem de ciclos e aciona o processador e a UI."""
        if self.count == 0:
            self.sys_class_exe_processador.exe_loop()
            self.front_enter.atualizar_processador_porcentagem()

    def _executar__uso_por_nucleo(self):
        """Gerencia a contagem de ciclos e aciona o uso por núcleo e a UI."""
        if self.count == 0:
            # exe_loop já foi executado em _executar__processador_porcentagem,
            # atualizando em conjunto a porcentagem total e a de cada núcleo.
            self.front_enter.atualizar_uso_por_nucleo()

    def _executar_ram_porcentagem(self):
        """Gerencia a contagem de ciclos e aciona a RAM e a UI."""
        if self.count == 0:
            self.sys_class_exe_ram.exe_loop()
            self.front_enter.atualizar_memoria_ram()

    def __executar_temperatura_wifi(self):
        """Gerencia a contagem de ciclos e aciona a temperatura do Wi-Fi e a UI."""
        if self.count == 0:
            self.sys_class_exe_temperatura.exe_loop()

            self.front_enter.atualizar_temperatura_wifi()
            self.front_enter.atualizar_temperatura_placa_mae()
            self.front_enter.atualizar_temperatura_perifericos()
            self.front_enter.atualizar_temperatura_cpu_media()

    def __count_ciclos(self):
        """Gerencia a contagem de ciclos para determinar quando executar ações."""
        self.count += 1
        intervalo = TemporizadorCiclos.obter_intervalo_segundos()

        if self.count >= intervalo:
            self.count = 0

    def __externo(self):

        self.sys_class_bateria.exec_bateria()

    def __front_enter_janelamain(self):

        self.front_enter.atualizar_bateria()
