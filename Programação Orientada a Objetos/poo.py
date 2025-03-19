from exception import Type
import json

dictionaty = {}

class Especialidade:
    def __init__(self,area):
        self.area = area

class Empresa:
    def __init__(self,id,name,ceo,headquarters,capital,area,contact=None,active=True):
        self.__id =id
        self.name = name
        self.ceo = ceo
        self.headquarters = headquarters
        self.active = active
        self.capital = capital
        self.area = area
        self.contact = contact
        self.lista = []
        
 
    @property
    def get_name(self):
        return f"Nome da Empresa : {self.name}"
    
    @get_name.setter
    def alter_id(self,new):
        if type(new):
            raise Type('O nome deve ser composto por letras')
        else:
            self.name = new 

    def listagem(self):
        self.lista.append(self.__id)
        self.lista.append(self.name)
        self.lista.append(self.ceo)
        self.lista.append(self.headquarters)
        self.lista.append(self.active)
        self.lista.append(self.capital)
        self.lista.append(self.area)
        self.lista.append(self.contact)
        return self.lista 
    



class Funcionario:
    def __init__(self,name,wage,enterprise,result,profession):
        self.name = name 
        self.__wage = wage
        self.enterprise = enterprise
        self.profession = profession
        self.result = result
        self.caracteristicas = dictionaty
        
        dictionaty['Funcionário(a)'] = self.name
        dictionaty['Salário'] = self.__wage
        dictionaty['Resultados'] = self.result
        dictionaty['Empresa'] = self.enterprise
        dictionaty['Profissão'] = self.profession
       
        
    @property
    def getter(self):
        return self.name
    
    def aumento(self,aumento):
            if dictionaty['Resultados'] >= 50:
                self.__wage = self.__wage +(self.__wage*(aumento/100))
                return f'{self.__wage:.2f}'
            else:
                print(f'O salário do funcionário {self.name} permanecerá o mesmo, pois os resultados não foram atingidos!')

    
    def add_info(self):
        self.name = str(input(""))

class Departamento:
    def __init__(self,nome,id,tipo):
        self.nome = nome  
        self.__id= id
        self.tipo = tipo

    def responsavel(self,responsavel):
      self.encarregado = responsavel

    
    def faturamento(self,money):
      self.money = money
      return f'O departamento {self.nome} teve nessa semana um faturamento {self.money}'

class Profissional_Tecnologia(Funcionario):
    def __init__(self,name,wage,enterprise,profession,result,formation,speciality):
      super().__init__(name,wage,enterprise,result,profession)
      self.formation = formation
      self.speciality = speciality
      self.projects = []

    def add_projects(self,project):
        self.projects.append(project)
        return f"O funcionário {self.name} ajudou nos seguintes projetos\n {self.projects}"

class Profissional_Atendimento(Funcionario):
    def __init__(self, name, wage, enterprise, result, profession,phone):
        super().__init__(name, wage, enterprise, result, profession)
        self.phone = phone

    #def informations(self):
       # with open("Informações.json",'r') as archive:
               


#Criação dos objetos

tech = Especialidade('Tecnologia,Serviços de Computação em Nuvem')
amazon = Empresa(4,'Amazon Web Services',"Jeff bezos","Seattle,Washington",'US$ 11 trilhões',tech,1452214899)
print(amazon)
marcos = Profissional_Tecnologia('Marcos Lorenzo',4000,'Lojas Besni','Desenvolvedor Web',44,'Faculdade Impacta','Front-End(HTML,CSS,JavaScript)')
marcos_projeto1=marcos.add_projects('Bot de leitura de email simultaneos')
project2 = marcos.add_projects("Site de vendas de cosméticos")
print(project2)

lista = amazon.listagem()
print(lista)
"""amazon = Empresa(7,'Amazon','Jeff Bezos','Seattle,Washington','R$ 11 trilhões','Tecnologia',596521458)
microsoft = Empresa(4,'Microsoft','Bill gates','Washington','US$ 2,44 trilhões','Informática',945566632)
cinemark = Empresa(41,'Cinemark','Mark Zoradi','Plano,Texas','US$ 734 milhões','Filmes',999996545)
votoran = Empresa(154,'Cimentos Votoran','Leonardo','Pindamonhangaba,SP','R$ 254 Milhões','Construção civil',6595854123,False)"""

#rh = Departamento('Departamento RH Soluções',55,'Administrativo')
#rh.responsavel("Karolina junior alves")

#reginaldo = Profissional_Tecnologia("Reginaldo nogueira",2999,'Amazon','Desenvolvedor Full-Stack',44,'Faculdade UNIP','Full stack,Banco de dados, e Backend')


#jose= Funcionario('José Andrade dos anjos',2520,'Akzell ',80,'Operador de máquinas')
#jose.aumento(47)
#aument = jose.aumento(6)
#print(aument)
#m = microsoft.get_id
#cod = amazon.get_id
#cine=cinemark.get_id
#amz = amazon.listagem()
#cinema_list= cinemark.listagem()
#print(amz)
#print(cinema_list)