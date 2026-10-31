# mainwindows
# processador
from mainwindows.ui.processador.stack import StackProcessador
from mainwindows.ui.processador.grid import GridProcessador
# ram
from mainwindows.ui.memoria_ram.stack_ram import StackRam
from mainwindows.ui.memoria_ram.uso_ram import UsoRam

# mamorias
from memoria.processador import MemoriaProcessador
from memoria.ram import MemoriaRam


class FrontEnter:

    def __init__(self) -> None:

        self.mm_class_var_porcentagem = MemoriaProcessador()
        self.mm_class_var_memoria_ram = MemoriaRam()

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

    def atualizar_memoria_ram(self):
        # Lógica para atualizar a memória RAM

        dados_ram = self.mm_class_var_memoria_ram.get_lista_ram()[0]
        uso_ram = UsoRam.get_instancia()
        if uso_ram:
            uso_ram.atualizar_total_ram(
                dados_ram["memoria_usada"],
                dados_ram["total_memoria"],
            )

        stack_ram = StackRam.get_instancia()
        if stack_ram:
            stack_ram.set_calculo(dados_ram["porcentagem"])
