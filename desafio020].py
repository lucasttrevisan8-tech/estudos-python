from rich import print
from rich.panel import Panel
from rich import inspect
from rich.table import Table
from rich.traceback import install
install()
class Gamer:
    def __init__ (self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted (self.favoritos, key=str.lower)#Essa linha serve para ordenar os dados em ordem alfabética

    def ficha(self):
        conteudo = f"Nome real: [black on cyan] {self.nome} [/]"
        conteudo +=f"\nJogos Favoritos:\n"
        for num, game in enumerate(self.favoritos):
            conteudo += f":video_game: [blue]{game}[/]\n"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print (painel)

j1 = Gamer ("Lucas", "TrevisanNinja")
j1.add_favoritos("Clash Royale")
j1.add_favoritos("God of War_Ragnarok")
j1.add_favoritos("Minecraft")
j1.add_favoritos("Call of Duty")
j1.ficha()

j2 = Gamer ("Maria", "Princesa_raivosa")
j2.add_favoritos("Roblox'Parkour'")
j2.add_favoritos("Minecraft")
j2.add_favoritos("Empurra porco")
j2.ficha()


