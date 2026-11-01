import psutil


class Temperatura:
    """Le os chips de temperatura encontrados por ``psutil``."""

    def __init__(self) -> None:
        self.temperatura = {}

    def _obter_entradas_sensor(self, nome: str):
        """Localiza um chip pelo nome ou por um nome com sufixo (ex.: iwlwifi_1)."""
        self.temperatura = psutil.sensors_temperatures()
        if not self.temperatura:
            raise LookupError("O sistema não retornou sensores de temperatura.")

        nome_sensor = next(
            (
                chave
                for chave in self.temperatura
                if chave == nome or chave.startswith(f"{nome}_")
            ),
            None,
        )
        if nome_sensor is None:
            raise LookupError(
                f"Sensor '{nome}' não encontrado. "
                f"Sensores disponíveis: {', '.join(self.temperatura)}."
            )
        return nome_sensor, self.temperatura[nome_sensor]

    def _ler_sensor(self, nome: str, indice: int = 0):
        """Retorna [True, temperatura] ou [False, erro]."""
        try:
            nome_sensor, sensores = self._obter_entradas_sensor(nome)
            if indice >= len(sensores):
                raise LookupError(
                    f"O sensor '{nome_sensor}' não possui uma entrada no índice {indice}."
                )

            valor = sensores[indice].current
            if valor is None:
                raise ValueError(f"O sensor '{nome_sensor}' não retornou temperatura.")
            return [True, valor]
        except Exception as erro:
            return [False, erro]

    def _ler_lista_sensor(self, nome: str):
        """Retorna [True, lista_de_temperaturas] para todas as entradas do chip."""
        try:
            nome_sensor, sensores = self._obter_entradas_sensor(nome)
            valores = [
                sensor.current
                for sensor in sensores
                if sensor.current is not None
            ]
            if not valores:
                raise ValueError(f"O sensor '{nome_sensor}' não retornou temperaturas.")
            return [True, valores]
        except Exception as erro:
            return [False, erro]

    def temperatura_cpu(self):
        # Retorna Package id 0 e as temperaturas de cada núcleo.
        return self._ler_lista_sensor("coretemp")

    def placa_mae(self):
        # Retorna todas as leituras disponibilizadas por acpitz.
        return self._ler_lista_sensor("acpitz")

    def wifi_temperatura(self):
        # Localiza iwlwifi e também nomes sufixados, como iwlwifi_1.
        return self._ler_sensor("iwlwifi")

    def perifericos(self):
        # Retorna a leitura principal do chipset/periféricos.
        return self._ler_sensor("pch_cannonlake")
