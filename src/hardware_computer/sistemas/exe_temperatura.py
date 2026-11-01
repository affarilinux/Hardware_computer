from unittest import result

from externo.temperatura import Temperatura
from memoria.temperatura import (Temperaturawifi, MnPlacaMae,
                                 MnPerifericos, MnCpu)


class WifiTemp:

    def __init__(self) -> None:
        super().__init__()
        self.var_temperatura_wifi = Temperaturawifi()

    def wifi_temperatura(self):
        # Evite usar double underscore (__) para variáveis locais simples
        status_valor = self.sys_class_exetemperatura.wifi_temperatura()

        # Otimização da lógica de verificação
        if status_valor[0]:  # Em Python, não precisa testar '== True'
            status = True
            valor = status_valor[1]
        else:
            status = False
            valor = 0

        self.var_temperatura_wifi.set_status(status)
        self.var_temperatura_wifi.set_temperatura(valor)


class PlacaMaeTemp:

    def __init__(self) -> None:
        super().__init__()
        self.var_temperatura_placa_mae = MnPlacaMae()

    def placa_mae_temperatura(self):
        status_valor_pm = self.sys_class_exetemperatura.placa_mae()

        if status_valor_pm[0]:  # Em Python, não precisa testar '== True'
            status_pm = True
            valor = status_valor_pm[1]

            soma = 0
            media = 0
            for result in valor:
                soma += result
            media = round(soma / len(valor), 2)

        else:
            status_pm = False
            valor = []
            media = 0

        self.var_temperatura_placa_mae.set_status_mn(status_pm)
        self.var_temperatura_placa_mae.set_temperatura_media(media)
        self.var_temperatura_placa_mae.set_list_temperatura(valor)


class PerifericosTemp:

    def __init__(self) -> None:
        super().__init__()
        self.var_temperatura_perifericos = MnPerifericos()

    def perifericos_temperatura(self):
        status_valor_pf = self.sys_class_exetemperatura.perifericos()

        if status_valor_pf[0]:  # Em Python, não precisa testar '== True'
            status_pf = True
            valor = status_valor_pf[1]

        else:
            status_pf = False
            valor = 0

        self.var_temperatura_perifericos.set_status_perifericos(status_pf)
        self.var_temperatura_perifericos.set_temperatura(valor)


class CpuTemp:

    def __init__(self) -> None:
        super().__init__()
        self.var_temperatura_cpu = MnCpu()

    def cpu_temperatura(self):
        status_valor_cpu = self.sys_class_exetemperatura.temperatura_cpu()

        if status_valor_cpu[0]:  # Em Python, não precisa testar '== True'
            status_cpu = True
            valor = status_valor_cpu[1]

            soma = 0
            media = 0
            for result in valor:
                soma += result
            media = round(soma / len(valor), 2)

        else:
            status_cpu = False
            valor = []
            media = 0
        self.var_temperatura_cpu.set_status_cpu(status_cpu)
        self.var_temperatura_cpu.set_temperatura_media(media)
        self.var_temperatura_cpu.set_lista_temperatura(valor)


class ExeTemperatura(WifiTemp, PlacaMaeTemp, PerifericosTemp, CpuTemp):

    def __init__(self) -> None:
        super().__init__()
        # Agora o atributo da classe pai é devidamente preenchido
        self.sys_class_exetemperatura = Temperatura()

    def exe_loop(self):
        """
        Atualização de lista pelo loop.
        """
        self.wifi_temperatura()
        self.placa_mae_temperatura()
        self.perifericos_temperatura()
        self.cpu_temperatura()
