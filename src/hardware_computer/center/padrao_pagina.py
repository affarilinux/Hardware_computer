from flet import Colors


class PadraoPagina:

    def tamanho_tela(self, pagina):

        # largura
        pagina.window.width = 500
        # altura
        pagina.window.height = 768

    def cor_fundo_pagina(self, page):

        page.bgcolor = "#121212"  # cinza muito escuro

    def titulo_pagina(self, page):

        page.title = "Monitoramento de Hardware"
