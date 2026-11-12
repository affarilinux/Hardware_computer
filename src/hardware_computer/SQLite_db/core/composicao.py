
from SQLite_db.core.conexao import ConexaoSqlite


class SqliteComposicao(ConexaoSqlite):

    def tabelas_criacao(self):

        self.__temporizador_ciclo()

    def __ativar(self):

        self.ativar_with()

    def __executar(self, query):

        self.with_executar_query(query)

    def __temporizador_ciclo(self):

        self.__ativar()

        query = """
                CREATE TABLE IF NOT EXISTS  temporizador_ciclos(

                ID_ciclos INTEGER PRIMARY KEY AUTOINCREMENT,

                ciclo  INT
                )

            """

        self.__executar(query)
