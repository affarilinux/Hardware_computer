
class MemoriaRam:

    _memoria_ram = {
        "status": False,
        "total_memoria": 0,
        "memoria_usada": 0,
        "porcentagem": 0
    }

    def set_status(self, status: bool):
        self._memoria_ram["status"] = status

    def set_total_memoria(self, total_memoria: int):
        self._memoria_ram["total_memoria"] = total_memoria

    def set_memoria_usada(self, memoria_usada: int):
        self._memoria_ram["memoria_usada"] = memoria_usada

    def set_porcentagem(self, porcentagem: float):
        self._memoria_ram["porcentagem"] = porcentagem

    def get_lista_ram(self) -> list:
        # Retorna uma cópia ou o próprio dicionário estruturado em lista
        return [self._memoria_ram]
