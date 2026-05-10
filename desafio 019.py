from rich import print
from rich.panel import Panel
from rich.table import Table
import time
from rich.traceback import install
install()

class Livro:

    def __init__ (self, nome, paginas):
        self.nome = nome
        self.total_paginas = paginas
        self.pagina_atual = 1
        print (f":open_book: Você acabou de abrir o livro [purple]{self.nome}[/], que tem um "
               f"total de [blue]{self.total_paginas} páginas[/], [yellow]e agora está na página {self.pagina_atual}[/]")

    def passar_paginas (self, qtd = 1):
        cont = 0
        for pg in range (0, qtd, 1):
            if  not  self.fim_do_livro():
                     self.pagina_atual += 1
                     print (f"Pág{self.pagina_atual} :arrow_forward: ", end = '')
                     time.sleep (0.2)
                     cont += 1
        print (f"[blue]Você avançou um total de {cont} páginas[/],[yellow]Você está na página {self.pagina_atual} "
               f"agora[/]")
        if self.fim_do_livro():
            print (f":closed_book: [red] Você chegou ao final do livro,[purple]'{self.nome}'[/][/red], [purple]não precisa mais passar "
                   f"páginas caro leitor[/]. [green]Agradeço a leitura[/]")


    def fim_do_livro (self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False

#posso fazer dessa forma abaixo ou da que  está acima
#if self.pagina_atual == self.total_paginas
##return True
#else:
#return False



l1 = Livro ("pessoas", 15)
l1.passar_paginas(15)

l2 = Livro ("como ser melhor", 30)
l2.passar_paginas (10)
l2.passar_paginas(10)
l2.passar_paginas(15)

