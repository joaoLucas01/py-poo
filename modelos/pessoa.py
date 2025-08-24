class Pessoa :
    pessoas = []
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self._nome} é {self.profissao} tem {self.idade} anos'
    
    def aniversario(self):
        self.idade += 1
    @classmethod
    def listar_pessoas(cls):
        for pessoa in cls.pessoas:
            print(f'{pessoa._nome} | {pessoa.idade} | {pessoa.profissao}')
            
joao_lucas = Pessoa('João Lucas', '13', 'profissao')

Pessoa.listar_pessoas()
