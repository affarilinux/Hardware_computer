class MemoriaProcessador:
    # Atributo de classe (compartilhado globalmente)
    _dados_compartilhados = {
        "status": False,
        "porcentagem": 0
    }

    _nucleo_cpu = {
        "status": False,
        "uso_por_nucleo": 0
    }

    """
    porcentagem cpu
    """

    def set_status(self, status: bool):
        self._dados_compartilhados["status"] = status

    def set_porcentagem(self, porcentagem: int):
        self._dados_compartilhados["porcentagem"] = porcentagem

    def get_lista(self) -> list:
        # Retorna uma cópia ou o próprio dicionário estruturado em lista
        return [self._dados_compartilhados]

    """
    uso por nucleo cpu
    """

    def set_status_nucleo(self, status: bool):
        self._nucleo_cpu["status"] = status

    def set_uso_por_nucleo(self, uso_por_nucleo: list):

        self._nucleo_cpu["uso_por_nucleo"] = uso_por_nucleo

    def get_lista_nucleo(self) -> list:
        # Retorna uma cópia ou o próprio dicionário estruturado em lista
        return [self._nucleo_cpu]
