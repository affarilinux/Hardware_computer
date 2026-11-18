from SQLite_db.core.conexao import ConexaoSqlite


class SelectCiclos(ConexaoSqlite):

    def get_selecionar_ciclo_linha_1(self):

        self.ativar_banco()

        select_query = """
                    SELECT ciclo FROM temporizador_ciclos LIMIT 1;
        
                """
        self.cursor_executar_query(select_query)
        select_ciclos_1 = self.select_uma_linha()
        self.sair_banco()

        return select_ciclos_1[0] if select_ciclos_1 else None
