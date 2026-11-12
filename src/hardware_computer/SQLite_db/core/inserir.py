from SQLite_db.core.conexao import ConexaoSqlite

class Inserir(ConexaoSqlite):

    def verificar_tabela(self):

    def __temporizador_ciclos(self):

        self.ativar_banco()

        query = """
            SELECT ciclo FROM temporizador_ciclos LIMIT 1;

        """