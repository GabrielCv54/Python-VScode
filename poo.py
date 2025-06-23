class Player:
    def __init__(self,name,age,game,points):
        self.name = name
        self.age = age
        self.game = game
        self.points = points

    def __str__(self):
        return f'{self.name},{self.age},{self.game},{self.points}'
    
player = Player('pedro',25,'Xadrez',225)
print(player)


class Student:
    def __init__(self,name,idade,materia_fav,turma,escola,profissao):
        self.nome = name
        self.idade = idade 
        self.materia = materia_fav
        self.turma = turma
        self.escola = escola
        self.futura_profissao = profissao

    def __str__(self):
        print('='*40)
        return f' Nome:{self.nome}\n Idade:{self.idade}\n Matéria Favorita:{self.materia}\n Turma:{self.turma}\n Escola:{self.escola}\n Profissão Desejada:{self.futura_profissao}'
class Gabriel:
  def __init__(self,name,idade,materia_fav,turma,escola,profissao,faculdade):
      super().__init__(name,idade,materia_fav,escola,turma,profissao)
      self.faculdade = faculdade

g = Student('Henrique',17,'Linguagens','3°C','Mackenzie','Design de interiores')
print(g.__str__())


empresas=['Microsoft','Amazon','IBM','RedHat','samsung']
people={'Nome':'Joe ','Idade':55,'Cidade':'San jose','Nacionalidade':'Americano(USA)'}

iteration = iter(empresas)
print(next(iteration))