# mainwindows
from mainwindows.ui.processador.stack import StackProcessador

# mamorias
from memoria.processador import MemoriaProcessador


class FrontEnter:

    def atalizar_processador_porcentagem(self):
        # Lógica para atualizar a porcentagem do processador

        stack_proc = StackProcessador.get_instancia()
        if stack_proc:

            mm_class_var_porcentagem = MemoriaProcessador()
            var_pc = mm_class_var_porcentagem.get_lista()[0]["porcentagem"]
            stack_proc.set_calculo(
                var_pc
            )
