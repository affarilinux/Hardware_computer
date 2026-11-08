import flet as ft
import flet.canvas as cv


class WidgetGrafico:

    def __init__(self) -> None:
        self.wdg_grafico = self._criar_grafico()
        self.wdg_grafico.visible = False

    def _criar_grafico(self):
        largura = 440
        altura = 265
        categorias = ["A", "B", "C", "D", "E", "F", "G", "H"]
        series = [
            ("Série 1", [500, 2900, 2550, 4050, 3450, 5900, 5650, 6650], "#3288E8"),
            ("Série 2", [5200, 6100, 4100, 2850, 2550, 1700, 1450, 1100], "#FF9900"),
            ("Série 3", [6400, 7700, 5300, 2550, 4500, 2300, 3600, 2100], "#18C6B3"),
        ]

        formas = []
        faixa = largura / len(categorias)
        for indice in range(len(categorias)):
            formas.append(
                cv.Rect(
                    x=indice * faixa,
                    y=0,
                    width=faixa,
                    height=altura,
                    paint=ft.Paint(
                        color="#F1F2F2" if indice % 2 == 0 else "#E4E6E7",
                        style=ft.PaintingStyle.FILL,
                    ),
                )
            )

        incremento_x = largura / (len(categorias) - 1)
        for _, valores, cor in series:
            tinta = ft.Paint(color=cor, stroke_width=2.2)
            pontos = [
                (indice * incremento_x, altura * (1 - valor / 8000))
                for indice, valor in enumerate(valores)
            ]
            for ponto_atual, proximo_ponto in zip(pontos, pontos[1:]):
                formas.append(
                    cv.Line(
                        x1=ponto_atual[0],
                        y1=ponto_atual[1],
                        x2=proximo_ponto[0],
                        y2=proximo_ponto[1],
                        paint=tinta,
                    )
                )

        grafico = cv.Canvas(width=largura, height=altura, shapes=formas)
        rotulos_y = ft.Column(
            controls=[
                ft.Text(str(valor), size=11, color="#F2F2F2")
                for valor in range(8000, 0, -1000)
            ],
            width=42,
            height=altura,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.END,
        )
        rotulos_x = ft.Stack(
            width=largura,
            height=20,
            controls=[
                ft.Container(
                    content=ft.Text(categoria, size=11, color="#F2F2F2"),
                    left=max(
                        0,
                        min(largura - 20, indice * incremento_x - 10),
                    ),
                    width=20,
                    alignment=ft.Alignment.CENTER,
                )
                for indice, categoria in enumerate(categorias)
            ],
        )
        legenda = ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(width=20, height=3, bgcolor=cor),
                        ft.Text(nome, size=11, color="#F2F2F2"),
                    ],
                    spacing=6,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
                for nome, _, cor in series
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=16,
        )

        return ft.Column(
            controls=[
                ft.Text("Valor (0–8000)", size=11, color="#F2F2F2"),
                ft.Row(
                    controls=[rotulos_y, grafico],
                    spacing=4,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    controls=[ft.Container(width=42), rotulos_x],
                    spacing=4,
                ),
                ft.Text("Categoria", size=11, color="#F2F2F2"),
                legenda,
            ],
            spacing=4,
            tight=True,
        )

class Grafico(WidgetGrafico):

    def get_grafico(self):
        return self.wdg_grafico
