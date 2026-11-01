import psutil


class Temperatura:
    """Le temperaturas expostas pelos sensores do sistema via psutil."""

    def __init__(self) -> None:
        self.temperatura = {}

    def _ler_sensor(self, nome: str, indice: int = 0):
        """Retorna [True, valor] ou [False, erro] para manter a API existente."""
        try:
            self.temperatura = psutil.sensors_temperatures()
            # O psutil pode acrescentar um sufixo ao nome do chip, por
            # exemplo ``iwlwifi_1`` em vez de ``iwlwifi``.
            nome_sensor = next(
                (
                    chave
                    for chave in self.temperatura
                    if chave == nome or chave.startswith(f"{nome}_")
                ),
                None,
            )
            sensores = self.temperatura.get(nome_sensor, []) if nome_sensor else []

            if indice >= len(sensores):
                raise LookupError(
                    f"Sensor '{nome}' não encontrado no índice {indice}. "
                    f"Sensores disponíveis: {', '.join(self.temperatura.keys()) or 'nenhum'}."
                )

            valor = sensores[indice].current
            if valor is None:
                raise ValueError(f"O sensor '{nome}' não retornou temperatura.")

            return [True, valor]
        except Exception as erro:
            return [False, erro]

    def temperatura_cpu(self):
        return self._ler_sensor("coretemp")

    def placa_mae(self):
        return self._ler_sensor("acpitz")

    def wifi_temperatura(self):
        return self._ler_sensor("iwlwifi")

    def perifericos(self):
        return self._ler_sensor("pch_cannonlake")
