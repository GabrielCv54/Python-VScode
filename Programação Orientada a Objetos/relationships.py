#Associação

class Escritor:
    def __init__(self,nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    

#Dependência
class Impressora:
    def imprimir(self,documento):
        print(f'Imprimindo : {documento}')

class User:
    def solicitação(self,impressora,documento):
        impressora.imprimir(documento)

deskjet = Impressora()
Gabriel = User()
Gabriel.solicitação(deskjet,"Papel pra colorir")


#Agregação
class Jogador:
    def __init__(self,nome):
        self.nome = nome

class Time:
    def __init__(self,nome):
        self.nome = nome
        self.jogadores=[]

    def add_jogador(self,jogador):
        self.jogadores.append(jogador)
    
cr7 = Jogador('Cristiano Ronaldo')
real = Time('Real Madrid')
real.add_jogador(cr7)
print(real.jogadores)

#Composição
class Quarto:
  def __init__(self,nome):
      self.nome = nome

class Casa:
    def __init__(self,address):
        self.endereco = address
        self.quarto_casal = Quarto("Quarto casal")