import asyncio

# sistemas
from sistemas.exe_processador import ExeProcessador
# mainwindows
from mainwindows.front_enter import FrontEnter


class BackAssincrono:

    def __init__(self) -> None:
        self.sys_class_exe_processador = ExeProcessador()
        self.front_enter = FrontEnter()

        # contagem de ciclos
        self.count_processador = 0

    async def iniciar_loop_background(self):
        """Loop principal executado em segundo plano a cada 1 segundo."""
        while True:
            self._executar__processador_porcentagem()
            await asyncio.sleep(1)

    def _executar__processador_porcentagem(self):
        """Gerencia a contagem de ciclos e aciona o processador e a UI."""
        if self.count_processador == 0:
            self.sys_class_exe_processador.exe_loop()
            self.front_enter.atalizar_processador_porcentagem()
            self.count_processador += 1
        else:
            self.count_processador += 1
            if self.count_processador == 10:
                self.count_processador = 0
