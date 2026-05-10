from rich import print
from rich import inspect
from rich.panel import Panel
from rich.traceback import install
install()

class Produto:

    def __init__ (self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__ (self):
        return f"{self.nome} custa R${self.preco:,.2f}"

    def etiqueta (self):
        conteudo = (f"[red]{self.nome.center(30, ' ')}[/]")
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"[green]{precof.center(30, '.')}[/]"
        etiqueta = Panel (conteudo, title="Produto", width=34)
        print (etiqueta)

p1 = Produto ("iPhone 17 pro max", 10_000)
p1.etiqueta()

p2 = Produto ("Notebook Apple", 15_000)
p2.etiqueta()

p3 = Produto ("Honda FIT", 70_000)
p3.etiqueta()
