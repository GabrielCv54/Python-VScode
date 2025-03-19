class Retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura

    @property
    def largura(self):
        return self.__largura
    
    @largura.setter
    def largura(self)