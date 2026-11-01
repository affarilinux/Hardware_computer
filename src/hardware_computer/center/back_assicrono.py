import asyncio

# sistemas
from sistemas.exe_processador import ExeProcessador
from sistemas.exe_ram import ExeRam
# conjunto de classes
from sistemas.exe_temperatura import ExeTemperatura

# mainwindows
from mainwindows.front_enter import FrontEnter


class BackAssincrono:

    def __init__(self) -> None:
        self.sys_class_exe_processador = ExeProcessador()
        self.sys_class_exe_ram = ExeRam()
        self.sys_class_exe_temperatura = ExeTemperatura()
        self.front_enter = FrontEnter()

        # contagem de ciclos
        self.count = 0

    async def iniciar_loop_background(self):
        """Loop principal executado em segundo plano a cada 1 segundo."""
        while True:
            self._executar__processador_porcentagem()
            self._executar__uso_por_nucleo()
            self._executar_ram_porcentagem()
            self.__executar_temperatura_wifi()

            # Gerencia a contagem de ciclos
            self.__count_ciclos()

            await asyncio.sleep(1)

    def _executar__processador_porcentagem(self):
        """Gerencia a contagem de ciclos e aciona o processador e a UI."""
        if self.count == 0:
            self.sys_class_exe_processador.exe_loop()
            self.front_enter.atualizar_processador_porcentagem()

    def _executar__uso_por_nucleo(self):
        """Gerencia a contagem de ciclos e aciona o uso por núcleo e a UI."""
        if self.count == 0:
            self.sys_class_exe_processador.exe_loop()
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

    def __count_ciclos(self):
        """Gerencia a contagem de ciclos para determinar quando executar ações."""
        self.count += 1
        if self.count == 10:
            self.count = 0
