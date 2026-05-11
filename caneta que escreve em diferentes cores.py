from rich import print

class Caneta:
    def __init__ (self, cor = "azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case  "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever (self, msg):
        if self.tampada:
            print (f":prohibited: A {self.cor}caneta[/] está tampada")
        else:
            print (f"{self.cor}{msg} [/]", end='')

    def quebrar_linha (self, qtd = 1):
        print (f"\n" * qtd, end='')

    def tampar (self):
        self.tampada = True

    def destampar (self):
        self.tampada = False

c1 = Caneta ("azul")
c2 = Caneta ("vermelha")
c3 = Caneta ("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever ("Olá Mundo")
c1.quebrar_linha(1)
c2.escrever ("Deu Certo!")
c2.quebrar_linha(1)
c3.escrever ("Obrigado por ver até aqui! Você é demais :heartbeat:")

c2.tampar()
c3.tampar()

c1.quebrar_linha(2)
c1.escrever ("Agora apenas a caneta azul(c1) irá escrever, as outras estão tampadas, mesmo que eu tente escrever "
             "com elas")
c1.quebrar_linha(2)

c2.escrever("Não irá funcionar")
c3.escrever("Estão tampadas novamente") #As canetas precisam do comando "destampar" para funcionarem normalmente
