
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

        "temperatura": 0
    }

    def set_status_mn(self, status: bool):
        self._placa_mae["status"] = status
        

    def set_temperatura(self, temperatura: float):

        self._placa_mae["temperatura"] = temperatura

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
