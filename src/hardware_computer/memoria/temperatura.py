
class Temperaturawifi:

    _wifi = {
        "status": False,
        "temperatura": 0
    }

    def set_status(self, status: bool):
        self._wifi["status"] = status

    def set_temperatura(self, temperatura: float):
        self._wifi["temperatura"] = temperatura

    def get_wifi(self):

        return self._wifi


class MnPlacaMae:

    _placa_mae = {
        "status": False,
        "list_temperatura": [],
        "temperatura_media": 0
    }

    def set_status_mn(self, status: bool):
        self._placa_mae["status"] = status

    def set_temperatura_media(self, temperatura_media: float):

        self._placa_mae["temperatura_media"] = temperatura_media

    def set_list_temperatura(self, list_temperatura: list):
        self._placa_mae["list_temperatura"] = list_temperatura

    def get_placa_mae_mn(self):

        return self._placa_mae


class MnPerifericos:

    _perifericos = {
        "status": False,
        "temperatura": 0
    }

    def set_status_perifericos(self, status: bool):
        self._perifericos["status"] = status

    def set_temperatura(self, temperatura: float):
        self._perifericos["temperatura"] = temperatura

    def get_perifericos(self):

        return self._perifericos


class MnCpu:

    _cpu = {
        "status": False,
        "temperatura": [],
        "temperatura_media": 0
    }

    def set_status_cpu(self, status: bool):
        self._cpu["status"] = status

    def set_temperatura_media(self, temperatura_media: float):
        self._cpu["temperatura_media"] = temperatura_media

    def set_lista_temperatura(self, lista_temperatura: list):
        self._cpu["temperatura"] = lista_temperatura

    def get_cpu(self):

        return self._cpu
