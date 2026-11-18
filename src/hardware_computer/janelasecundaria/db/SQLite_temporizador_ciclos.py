
from SQLite_db.temporizador_ciclos.select_ciclos import SelectCiclos
from SQLite_db.temporizador_ciclos.update_ciclos import UpdateCiclos

class SQLiteTemporizadorCiclos:

    def __init__(self) -> None:

        self.j_class_celectciclos = SelectCiclos()
        self.j_class_uc = UpdateCiclos()

    def selecionar_linha_1(self):

        var_1 = self.j_class_celectciclos.get_selecionar_ciclo_linha_1()

        return var_1

    def atualizar_linha_1(self,numero):

        self.j_class_uc.atualizar_linha_1(numero)


