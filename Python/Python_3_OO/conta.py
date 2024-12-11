class Conta:
    """
    Classe Conta: Representa uma conta bancária com métodos para manipular saldo e realizar transações.
    
    Conceitos:
    - Classe: Define a estrutura e o comportamento de um objeto.
    - Objeto: É uma instância de uma classe, que armazena dados e permite a execução de métodos.
    - Atributos: São as características (ou propriedades) que um objeto possui.
    - Métodos: São as funções definidas dentro de uma classe que representam o comportamento de seus objetos.
    """

    def __init__(self, numero, titular, saldo, limite) -> None:
        """
        Método Construtor: Inicializa os atributos de um objeto da classe Conta.

        Args:
        - numero (int): Número da conta.
        - titular (str): Nome do titular da conta.
        - saldo (float): Saldo inicial da conta.
        - limite (float): Limite disponível para operações.
        
        O `self` é uma referência ao próprio objeto, permitindo acessar e modificar seus atributos.
        """
        # O método é chamado automaticamente ao criar uma instância da classe
        print("Construindo objeto... {}".format(self))  # Exibe uma mensagem indicando a criação do objeto
        self.numero = numero  # Atributo 'numero' armazena o número da conta
        self.titular = titular  # Atributo 'titular' armazena o nome do titular
        self.saldo = saldo  # Atributo 'saldo' armazena o saldo inicial
        self.limite = limite  # Atributo 'limite' armazena o limite da conta

    def extrato(self):
        """
        Método para exibir o saldo atual e o titular da conta.

        Este método usa os atributos do objeto para exibir as informações da conta.
        """
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
    """
    Método para adicionar um valor ao saldo da conta.

    Args:
    - valor (float): Valor a ser depositado.
    """
    self.saldo += valor  # Adiciona o valor ao saldo atual

    def sacar(self, valor):
        """
        Método para retirar um valor do saldo da conta.

        Args:
        - valor (float): Valor a ser retirado.
        """
        self.saldo -= valor  # Subtrai o valor do saldo atual


# Conceitos Adicionais:

# Criando um objeto da classe Conta:
# conta = Conta(123, "Celo", 55.0, 1000.0)
# O objeto 'conta' é uma instância da classe Conta. A variável 'conta' armazena uma referência ao objeto criado.

# Atributos:
# Os atributos (numero, titular, saldo, limite) são associados ao objeto criado e armazenam dados específicos dele.

# Referências:
# Uma variável como 'conta' é apenas uma referência ao objeto criado.
# Exemplo:
# outra_ref = conta  # As duas variáveis apontam para o mesmo objeto na memória.

# Garbage Collector:
# O Python possui um coletor de lixo (Garbage Collector) que remove objetos não utilizados da memória.
# Para "desreferenciar" um objeto, podemos atribuir a variável a None:
# outra_ref = None  # Agora, 'outra_ref' não aponta mais para o objeto 'conta'.

# Desreferenciamento:
# Se todas as variáveis que referenciam um objeto forem desreferenciadas, o objeto é removido automaticamente da memória.