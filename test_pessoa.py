import unittest
from pessoa import Pessoa

class TestePessoa(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    # Teste mudar nome
    def test_set_nome(self):
        nome = 'Danilo'
        sobrenome = 'Halfters'
        idade = 18

        pessoa_teste = Pessoa(nome, sobrenome, idade)

        novo_nome = 'Daniella'
        pessoa_teste.set_nome(novo_nome)

        self.assertTrue(
            pessoa_teste.get_nome() != f'{nome} {sobrenome}' and
            pessoa_teste.get_nome() == f'{novo_nome} {sobrenome}'
        )

    # Teste pegar nome
    def test_get_nome(self):
        nome = 'Danilo'
        sobrenome = 'Halfters'
        idade = 18

        pessoa_teste = Pessoa(nome, sobrenome, idade)

        self.assertTrue(False)

    # Teste pegar idade
    def test_get_idade(self):
        nome = 'Danilo'
        sobrenome = 'Halfters'
        idade = 18

        pessoa_teste = Pessoa(nome, sobrenome, idade)

        self.assertTrue(
            pessoa_teste.get_idade() == idade
        )