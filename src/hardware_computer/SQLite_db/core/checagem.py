from SQLite_db.core.conexao import ConexaoSqlite


class Checagem(ConexaoSqlite):

    def verificar_tabela(self):

        self.__temporizador_ciclos()

    def __temporizador_ciclos(self):

        self.ativar_banco()

        # A inicialização deve garantir especificamente o registro de ID 1.
        # LIMIT 1 pode retornar outro registro e não verificar essa linha.
        select_query = """
            SELECT 1 FROM temporizador_ciclos WHERE ID_ciclos = 1;
        """
        self.cursor_executar_query(select_query)
        select_ciclos_1 = self.select_uma_linha()

        if select_ciclos_1 == None:

            insert_query = """
            INSERT INTO temporizador_ciclos (ID_ciclos, ciclo) VALUES (1, ?);
            """
            var_insert_5 = (5,)

            self.cursor_execute_query_insert(insert_query, var_insert_5)

        self.commit_banco()
        self.sair_banco()
