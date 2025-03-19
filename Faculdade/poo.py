class Produto:
    def __init__(self,nome,preço,quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def adicionar(self,qtd):
        self.quantidade += qtd
    
    def remover(self,qtde):
        if self.quantidade >=qtde:
         self.quantidade-=qtde
        else:
         self.quantidade="Quantidade inválida!!"
    
    def init(self):
        print(f"Produto : {self.nome}")
        print(f"Preço : {self.preço}")
        print(f"Quantidade : {self.quantidade}")

p1=Produto("Mochila",150,100)
p1.remover(150)
p1.init()