class Restaurante :
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do resaturante'.ljust(25)} | {'Categoria'.ljust(25)} | Ativo')
        print(f'--------------------------------------------------------------')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑ 卐' if self._ativo else '☐ 卐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'italiano')

Restaurante.listar_restaurantes()