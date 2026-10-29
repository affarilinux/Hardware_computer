import math
from dataclasses import dataclass

import flet as ft
import flet.canvas as cv

# mainwindows.core
from mainwindows.core.cores import Cores

# core.ultils
from core.ultils.pag import Pagina


@dataclass
class config:
    # O componente fica dentro de um container de 170 x 150.
    SIZE: int = 170
    HEIGHT: int = 150
    STROKE_WIDTH: int = 14
    RADIUS: int = 60


class StackProcessadorWidget:

    def __init__(self):
        self.MW_CLASS_DC_CONFIG = config()
        self.cores = Cores()

        self.valor_atual = 0.0
        self.valor_maximo = 100.0

        self.size = self.MW_CLASS_DC_CONFIG.SIZE
        self.center_x = self.size / 2
        self.center_y = self.MW_CLASS_DC_CONFIG.HEIGHT / 2 + 5
        self.radius = self.MW_CLASS_DC_CONFIG.RADIUS

        self.bg_paint = ft.Paint(
            color="#2C333B",
            style=ft.PaintingStyle.STROKE,
            stroke_width=self.MW_CLASS_DC_CONFIG.STROKE_WIDTH,
            stroke_cap=ft.StrokeCap.ROUND,
        )

        self.value_paint = ft.Paint(
            color="#42A5F5",
            style=ft.PaintingStyle.STROKE,
            stroke_width=self.MW_CLASS_DC_CONFIG.STROKE_WIDTH,
            stroke_cap=ft.StrokeCap.ROUND,
        )

        self.WDG_CANVAS = cv.Canvas(
            width=self.size,
            height=self.MW_CLASS_DC_CONFIG.HEIGHT,
            shapes=[
                cv.Arc(
                    x=self.center_x - self.radius,
                    y=self.center_y - self.radius,
                    width=self.radius * 2,
                    height=self.radius * 2,
                    start_angle=math.pi,
                    sweep_angle=math.pi,
                    use_center=False,
                    paint=self.bg_paint,
                ),
                cv.Arc(
                    x=self.center_x - self.radius,
                    y=self.center_y - self.radius,
                    width=self.radius * 2,
                    height=self.radius * 2,
                    start_angle=math.pi,
                    sweep_angle=0,
                    use_center=False,
                    paint=self.value_paint,
                ),
            ],
        )

        self.WDG_CLASS_TEXT = ft.Text(
            value="0.0%",
            weight=ft.FontWeight.W_900,
            color=self.cores.get_cor_branca(),
            size=25,
        )

        self.WDG_CONTAINER = ft.Container(
            content=self.WDG_CLASS_TEXT,
            width=80,
            height=50,
            alignment=ft.Alignment.CENTER,
            top=self.center_y - 25,
            left=self.center_x - 40,
        )

        self.WDG_STACK = ft.Stack(
            width=self.size,
            height=self.MW_CLASS_DC_CONFIG.HEIGHT,
            controls=[
                self.WDG_CANVAS, 
                self.WDG_CONTAINER
                ],
        )

    def get_stack(self):
        return self.WDG_STACK


class StackProcessador(StackProcessadorWidget):

    _instancia = None

    def __init__(self):
        super().__init__()
        StackProcessador._instancia = self

    @classmethod
    def get_instancia(cls):
        return cls._instancia

    def set_calculo(self, valor):
        valor = max(0.0, min(float(valor), self.valor_maximo))
        self.valor_atual = valor

        self.WDG_CLASS_TEXT.value = f"{valor:.1f}%"

        percentual = valor / self.valor_maximo
        self.WDG_CANVAS.shapes[1].sweep_angle = math.pi * percentual

        Pagina.getpag().update()
