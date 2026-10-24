class MemoriaProcessador:
    # Atributo de classe (compartilhado globalmente)
    _dados_compartilhados = {
        "status": False,
        "porcentagem": 0
    }

    def set_status(self, status: bool):
        self._dados_compartilhados["status"] = status

    def set_porcentagem(self, porcentagem: int):
        self._dados_compartilhados["porcentagem"] = porcentagem

    def get_lista(self) -> list:
        # Retorna uma cópia ou o próprio dicionário estruturado em lista
        return [self._dados_compartilhados]
