class Conta:

    def __init__(self) -> None:  # funcao construtora
        # self é a referncia qsabe onde encontrar nosso objeto
        print("Contruindo objeto ...")
        self.numero = 123
        self.titular = "Celo"
        self.saldo = 55.0
        self.limite = 1000.0


# conta = Conta() referencia
# atributo
