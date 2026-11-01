import psutil


class ExBateria:
    """Le a bateria do sistema usando ``psutil``."""

    def __init__(self) -> None:
        self.bateria = None

    def _obter_bateria(self):
        """Obtém informações da bateria."""
        self.bateria = psutil.sensors_battery()
        lista_bateria = []
        if self.bateria:
            lista_bateria = [True, self.bateria]
        else:
            lista_bateria = [False, 0]

        return lista_bateria
