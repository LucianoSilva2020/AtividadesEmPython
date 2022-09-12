class Cachorro:
    
    def __init__(self, nome, raca, alimentado, porte):
        self.__nome = nome
        self.__raca = raca
        self.__alimentado = alimentado
        self.__porte = porte

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome