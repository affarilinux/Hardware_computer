# mainwindows
from mainwindows.ui.processador.stack import StackProcessador
from mainwindows.ui.processador.grid import GridProcessador

# mamorias
from memoria.processador import MemoriaProcessador


class FrontEnter:

    def __init__(self) -> None:

        self.mm_class_var_porcentagem = MemoriaProcessador()

    def atualizar_processador_porcentagem(self):
        # Lógica para atualizar a porcentagem do processador

        stack_proc = StackProcessador.get_instancia()
        if stack_proc:

            var_pc = self.mm_class_var_porcentagem.get_lista()[
                0]["porcentagem"]
            stack_proc.set_calculo(
                var_pc
            )

    def atualizar_uso_por_nucleo(self):
        # Lógica para atualizar o uso por núcleo do processador

        # Atualiza o grid criado pelo ListaContainer e já exibido no front.
        grid_proc_nucleo = GridProcessador.get_instancia()
        if grid_proc_nucleo:

            var_nc = self.mm_class_var_porcentagem.get_lista_nucleo()[0][
                "uso_por_nucleo"]

            grid_proc_nucleo.for_processadores(
                var_nc
            )
