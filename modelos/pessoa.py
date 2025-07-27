class Pessoa :
    pessoas = []
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self._nome} tem {self.idade} anos'
    
    def aniversario
    
