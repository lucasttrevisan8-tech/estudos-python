from rich import inspect
from rich import print
from rich.traceback import install
install() #ESSA É MINHA BIBLIOTECA INSTALADA

class Funcionario: # ESSA É MINHA CLASSE
    """
    A 'class Funcionario' cria uma descrição de um funcionário que trabalha na empresa "AgroTrevisan", permite conhecer
    o  nome, setor, idade e cargo do funcionário pedido.
    """ #ESSA É MINHA DESCRIÇÃO DA CLASSE, PARA CASO QUEIRAM PEGAR

    empresa = "AgroTrevisan"

    def __init__ (self, nome, setor, cargo, idade = 0):
        #ATRIBUTOS DE INSTÂNCIA
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.idade = idade #ESSE ACIMA E MEU 'MÉTODO CONSTRUTOR'


    def apresentacao (self):
        return (f":handshake: Olá,sou o [red]{self.nome}[/], eu sou {self.cargo} do setor {self.setor} da empresa "
                f"{Funcionario.empresa} e tenho {self.idade} anos de idade")

c1 = Funcionario ("João", "Financeiro", "Contador", 20)  #ESSE É MEU OBJETO, O 'C1'
print (c1.apresentacao())
#inspect (c1, methods=True)

c2 = Funcionario ("Lucas", "tecnologia", "CTO", 28)
print (c2.apresentacao())
#inspect (c2, methods=True)

#inspect (Funcionario) ou posso usar 'inspect (Funcionario, all=True)


