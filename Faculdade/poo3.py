class Livro:
    def __init__(self, titulo, autor, ano, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponibilidade= disponibilidade
    def emprestar(self, disp):
        self.disponibilidade = disp
    def devolver(self, dev):
        self.disponibilidade = dev
    def info(self):
        print(f"Título  {self.titulo}")
        print(f"Autor : {self.autor}")
        print(f"Ano de Publicação : {self.ano}")
        print(f"Disponibilidade : {self.disponibilidade}")
    
l1= Livro('Magnus Chase','Rick riordan',2017,'Em uso')
l1.emprestar('Emprestado')
l1.info()