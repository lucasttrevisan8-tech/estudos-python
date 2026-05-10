from rich import print
from rich.traceback import install
from rich.table import Table
from rich.panel import Panel
install()

class Gado:

    valor_da_venda = 15000
    valor_do_matadouro = 5000
    valor_de_procriar = 10000

    def __init__ (self, titulo, ngado, dono):
        self.titulo = titulo
        self.ngado = ngado
        self.dono = dono

    def __str__ (self):
        return f"Essa é a tabela de {self.titulo} do Sr ou Sra {self.dono} e o total de cabeças é {self.ngado}"

    def vender (self):
        return self.valor_da_venda * self.ngado

    def matar (self):
        return self.valor_do_matadouro * self.ngado

    def procriar (self):
        return self.valor_de_procriar * self.ngado

    def analisar (self):
        conteudo = f"Analisando as opções do que se pode fazer com seu gado [red]sr {self.dono}[/]"
        conteudo +=f"\n"
        conteudo += (f"\nCaso o Sr[green] venda[/] o valor será de [yellow]R${self.valor_da_venda:,.2f}[/] por cabeça, caso venda "
                     f"tudo será de [yellow]R${self.vender():,.2f}[/]")
        conteudo += f"\n"
        conteudo += (f"\nAgora, caso decida mandar para o [red]matadouro[/], "
                     f"o valor de cada cabeça será de [yellow]R${self.valor_do_matadouro:,.2f}[/] caso decida mandar todos "
                     f"o calor será de [yellow]R${self.matar():,.2f}[/]")
        conteudo += f"\n"
        conteudo += (f"\nE caso decida [pink]procriar[/], o valor será de [yellow]R${self.valor_de_procriar:,.2f}[/] por gado,"
                     f"caso procrie todos, será de [yellow]R${self.procriar():,.2f}[/]")
        painel = Panel (conteudo, title=self.titulo)
        print (painel)

c1 = Gado ("Estratégias para o Gado", 5000, "Lucas")
c1.analisar()

c2 = Gado ("Gado do Sr Mateus", 6000, "Mateus")
c2.analisar()













