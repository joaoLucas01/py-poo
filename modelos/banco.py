class ContaBancaria:
    def __init__(self, titular, saldo, ativo):
        self._titular = titular.title
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self._titular} | {self.saldo}'
    
    conta1 = ContaBancaria('João', 2000)
    conta2 = ContaBancaria('Maria', 100)

    print(conta1)
    print(conta2)
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    conta3 = ContaBancaria('Flavio', '230000')

class ClienteBanco:
    pass
        