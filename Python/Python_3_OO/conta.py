class Conta:

    def __init__(self, numero, titular, saldo, limite) -> None:  # funcao construtora
        # self é a referncia q sabe onde encontrar nosso objeto
        print("Contruindo objeto... {}".format(self))
        self.numero = numero #123
        self.titular = titular #"Celo"
        self.saldo = saldo #55.0
        self.limite = limite #1000.0

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
# conta = Conta() referencia
# atributo
