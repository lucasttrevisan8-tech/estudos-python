from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 9
    volume_min:int = 1
    volume_max:int = 10

    def __init__ (self, canal = 1, volume = 1):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligada: bool = False


    def liga_desliga (self):
        self.ligada = not self.ligada

    def canal_mais (self):
        if self.ligada:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1



    def canal_menos (self):
        if self.ligada:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1


    def volume_mais (self):
        if self.ligada:
            if self.volume_atual != ControleRemoto.volume_max:
                 self.volume_atual += 1

    def volume_menos(self):
        if self.ligada:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1


    def mostrar_tv (self):

        conteudo = ''
        if not self.ligada:
            conteudo = f"[red]A TV está desligada[/]"

        else:
            conteudo = "CANAL  = "
            for canal in range(ControleRemoto.canal_min,ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "

            conteudo += f"\nVOLUME = "
            for volume in range (ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"


        tv=Panel (conteudo, title="[ TV ]", width=40)
        print (tv)

c1 = ControleRemoto ()
while True:
    c1.mostrar_tv()
    comando = str (input (f"< CH >  - VOL  +"))
    match comando:
        case '0':
            break
        case '@':
            c1.liga_desliga()
        case '>':
            c1.canal_mais()
        case '<':
            c1.canal_menos()
        case '-':
            c1.volume_menos()
        case '+':
            c1.volume_mais()
    print ("\n" * 10)