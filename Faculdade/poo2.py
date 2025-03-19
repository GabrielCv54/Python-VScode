class Pessoa:
    def __init__(self, nome, idade,endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço
    def alterar(self,end):
        self.endereço = end
    
    def info(self):
        print(f"Cliente : {self.nome}")
        print(f"Idade : {self.nome}")
        print(f"Endereço : {self.endereço}")

p=Pessoa("Dwayne", 25 , 'Rua albert guimaraes 365')
p.alterar("Rua tiradentes 72")
p.info()