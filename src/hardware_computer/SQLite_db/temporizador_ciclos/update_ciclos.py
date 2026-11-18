from SQLite_db.core.conexao import ConexaoSqlite


class UpdateCiclos(ConexaoSqlite):

    def atualizar_linha_1(self, numero):

        self.ativar_banco()

        select_query = """
            UPDATE temporizador_ciclos
            SET ciclo = ?
            WHERE ID_ciclos = 1;"""

        self.cursor_execute_query_duplo(select_query, numero)

        self.commit_banco()

        self.sair_banco()
