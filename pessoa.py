class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_nome(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def get_idade(self):
        return self.__idade