from rich import print
from rich import inspect
from rich.panel import Panel
from rich.traceback import install
install()

class Churrasco:
    #Atributos de classe
    preco_kg:float = 82.40 #Cada Kg de carne custa em média R$82,40
    consumo_padrao:float = 0.400 #Cada Pessoa come em média 400g de carne


    def __init__ (self, titulo, quant):
        #Atributos de instância
        self.titulo = titulo
        self.participantes = quant


    def __str__ (self):
        return f"Esse é o {self.titulo} com {self.participantes} pessoas"

    def calcular_qtd_carne (self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total (self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual (self) -> float:
        return self.calcular_custo_total() / self.participantes


    def analisar (self):
        conteudo = f"Analisando [purple]{self.titulo}[/] com [purple]{self.participantes} convidados [/]"
        conteudo += (f"\nCada participante comerá = [blue]{Churrasco.consumo_padrao}Kg[/], e cada Kg custa"
                     f"[yellow]R${Churrasco.preco_kg:,.2f}[/]")
        conteudo += f"\nRecomendo [red]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nE cada participante terá que pagar um total de [green]R${self.calcular_custo_individual():,.2f}[/]"
        painel = Panel (conteudo, title=self.titulo)
        print (painel)

c1 = Churrasco ("Churras dos Amigos", 15)
c1.analisar ()

c2 = Churrasco ("Churrasco de virada de ano", 98)
c2.analisar ()

c3 = Churrasco ("Churrasco para o fut", 23)
c3.analisar ()

c3 =Churrasco ("Churrasco de Aniversário", 22)
c3.analisar ()