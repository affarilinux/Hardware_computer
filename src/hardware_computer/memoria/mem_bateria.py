
class MemoriaBateria:

    _lista_bateria = {
        "status": False,
        "porcentagem": 0,
    }

    def set_status_bateria(self, status: bool):
        self._lista_bateria["status"] = status

    def set_porcentagem(self, porcentagem: float):
        self._lista_bateria["porcentagem"] = porcentagem

    def get_bateria(self):
        return self._lista_bateria
