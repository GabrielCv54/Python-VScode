'''
Criando um pequeno sistema como se fosse um jogo de tiro battle-royale,
onde são criados os soldados(Classe Soldier),
com seus métodos, e também as classes
'''
from sqlalchemy import create_engine, Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db = create_engine('sqlite:///battle_Royale.db')

class Soldier:
    def __init__(self,id,name,idade,nationality,armas):
        self.id = id
        self.name = name
        self.idade = idade
        self.nationality = nationality
        self.armas = armas
        self.habilidades = {}

    def add_habilidade(self,descrição,habilidade):
         self.habilidades[descrição] = habilidade

    def atacar(self,nome_inimigo,inimigo,atack):
       self.nome_inimigo = nome_inimigo
       self.inimigo = inimigo
       self.atack = atack
       while self.atack>0 or self.inimigo>0:
        if self.atack>self.inimigo:
            self.inimigo - self.atack
            print('Você venceu seu inimigo')
        elif self.inimigo > self.atack:
            self.atack - self.inimigo 
            print('Seu inimigo te eliminou!!')

    def main():
            
        
            while True:
                print('O que deseja?: ')
                print('1-Cadastrar um soldado para o jogo')
                print('2-Adicionar habilidade a um soldado: ')
                print('3- Iniciar combate escolhendo meu personagem')
                option = int(input('Escolha uma opção: '))
                if option == 1:
                    id=int(input('Código do(a) soldado(a): '))
                   # self.id = id
                    nome = str(input('Nome dele(a)'))
                  #  self.name = nome
                    idade = int(input('Idade: '))
                  #  self.idade = idade
                    nationality = str(input('Qual a nacionalidade?: '))
                 #   self.nationality = nationality
                    weapon=str(input('Qual a arma que ele usa?: '))
                  #  self.armas = weapon
                    hability=str(input('Quais são suas habilidades?: '))
                    description=str(input('Qual a descrição?: '))
                   # self.add_habilidade(description,hability)
                    more_h=str(input("Deseja adicionar mais alguma habilidade?: "))
                    while more_h == 'Sim'.lower() :
                        hability = str(input('Qual a outra habilidade: '))
                       # self.add_habilidade(description,hability)
                print(f'Informações do(a) competidor(a):')
                print(f'Nome:{nome}')
                print(f'Idade: {idade}')
                print(f'Nacionalidade: {nationality}')
                print(f'Arma : {weapon}')
                print(f'Habilidades: {hability}')
                
    if __name__ =='__main__':
        main()
    



class Inimigo(Soldier):
    def __init__(self, id, name, idade, nationality, armas, vitorias, derrotas,atack_enemy):
        super().__init__(id, name, idade, nationality, armas, vitorias, derrotas)
        self.atack_enemy = atack_enemy


class Exército: 
    def __init__(self,nome,lider):
        self.nome = nome
        self.membros = []
        self.lider = lider
    
    def add_or_remove_members(self,removed,add):
        self.removed = removed
        self.add = add
        if removed in self.membros:
            del removed
        else:
            print('O(a) soldado(a) não existe nos membros dessa organização!!')

    




loki = Soldier(0,'Loki daunen',33,'Tailandês',15,10)
loki.add_habilidade("")

