import sqlite3


class ConexaoSqlite:

    def __string_diretorio(self):

        __var_caminho = 'SQLite_db/core/hardware.db'

        return __var_caminho

    ##with___________________________-----------

    def ativar_with(self):

        # nao funciona update com commit()
        with sqlite3.connect(self.__string_diretorio()) as conn:

            self.withdb = conn.cursor()

    def with_executar_query(self,query):

        self.withdb.execute(query)


    ## banco var#############################
    def ativar_banco(self):

        self.conexao = sqlite3.connect(self.__string_diretorio())
        self.cursor = self.conexao.cursor()

    def commit_banco(self):

        self.conexao.commit()

    def sair_banco(self):

        self.cursor.close()
        self.conexao.close()

    def cursor_executar_query(self,query):

        self.cursor.execute(query)

    def select_uma_linha(self):

        self.cursor.fetchone()
