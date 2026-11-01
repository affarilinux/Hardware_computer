# mainwindows
# processador
from mainwindows.ui.processador.stack import StackProcessador
from mainwindows.ui.processador.grid import GridProcessador
# ram
from mainwindows.ui.memoria_ram.stack_ram import StackRam
from mainwindows.ui.memoria_ram.uso_ram import UsoRam
from mainwindows.ui.temperatura.linha_1 import Linha1
from mainwindows.ui.temperatura.linha_2 import Linha2
from mainwindows.ui.temperatura.cpu_temp import CpuTemp

# mamorias
from memoria.processador import MemoriaProcessador
from memoria.ram import MemoriaRam
from memoria.temperatura import MnPerifericos, MnPlacaMae, Temperaturawifi
from teste import temperatura


class FrontEnter:

    def __init__(self) -> None:

        self.mm_class_var_porcentagem = MemoriaProcessador()
        self.mm_class_var_memoria_ram = MemoriaRam()
        #conjunto de classes
        self.mm_class_temperatura_wifi = Temperaturawifi()
        self.mm_class_temperatura_placa_mae = MnPlacaMae()
        self.mm_class_perifericos = MnPerifericos()
        self.cpu_temp = CpuTemp()

    def atualizar_processador_porcentagem(self):
        # Lógica para atualizar a porcentagem do processador

        stack_proc = StackProcessador.get_instancia()
        if stack_proc:

            var_pc = self.mm_class_var_porcentagem.get_lista()[
                0]["porcentagem"]
            stack_proc.set_calculo(
                var_pc
            )

    def atualizar_uso_por_nucleo(self):
        # Lógica para atualizar o uso por núcleo do processador

        # Atualiza o grid criado pelo ListaContainer e já exibido no front.
        grid_proc_nucleo = GridProcessador.get_instancia()
        if grid_proc_nucleo:

            var_nc = self.mm_class_var_porcentagem.get_lista_nucleo()[0][
                "uso_por_nucleo"]

            grid_proc_nucleo.for_processadores(
                var_nc
            )

    def atualizar_memoria_ram(self):
        # Lógica para atualizar a memória RAM

        dados_ram = self.mm_class_var_memoria_ram.get_lista_ram()[0]
        uso_ram = UsoRam.get_instancia()
        if uso_ram:
            uso_ram.atualizar_total_ram(
                dados_ram["memoria_usada"],
                dados_ram["total_memoria"],
            )

        stack_ram = StackRam.get_instancia()
        if stack_ram:
            stack_ram.set_calculo(dados_ram["porcentagem"])


    def atualizar_temperatura_wifi(self):
        # Lógica para atualizar a temperatura do Wi-Fi

        temperatura_wifi = self.mm_class_temperatura_wifi.get_wifi()[
            "temperatura"]
        linha1 = Linha1.get_instancia()
        if linha1:
            linha1.set_wifi_temperatura(temperatura_wifi)

    def atualizar_temperatura_placa_mae(self):
        # Lógica para atualizar a temperatura da placa mãe

        temperatura_placa_mae = self.mm_class_temperatura_placa_mae.get_placa_mae_mn()[
            "temperatura"]
        linha1 = Linha1.get_instancia()
        if linha1:
            linha1.set_placa_mae_temperatura(temperatura_placa_mae)

    def atualizar_temperatura_perifericos(self):
        # Lógica para atualizar a temperatura dos periféricos

        temperatura_perifericos = self.mm_class_perifericos.get_perifericos()[
            "temperatura"]
        linha2 = Linha2.get_instancia()
        if linha2:
            linha2.set_perifericos_temperatura(temperatura_perifericos)

    def atualizar_temperatura_cpu_media(self):

        temperatura_cpu_media = temperatura.get_cpu_temperatura()[0][
            "temperatura_media"]


