class Conta:
    """
    Classe Conta: Representa uma conta bancária com métodos para manipular saldo e realizar transações.
    
    Conceitos:
    - Classe: Define a estrutura e o comportamento de um objeto.
    - Objeto: É uma instância de uma classe, que armazena dados e permite a execução de métodos.
    - Atributos: São as características (ou propriedades) que um objeto possui.
    - Métodos: São as funções definidas dentro de uma classe que representam o comportamento de seus objetos.
    """
    teste_de_atributo_simples = "É simples mesmo"
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
        self.__numero = numero  # Atributo 'numero' armazena o número da conta
        self.__titular = titular  # Atributo 'titular' armazena o nome do titular
        self.__saldo = saldo  # Atributo 'saldo' armazena o saldo inicial
        self.__limite = limite  # Atributo 'limite' armazena o limite da conta
        self.__codigo_banco = "001"

# No Python não existe private, mas podemos usar o underline para indicar que o atributo ou método deve ser tratado como privado.
# Isso é chamado de encapsulamento, onde as partes internas da classe podem ser acessadas, mas não devem ser modificadas diretamente.
# Encapsulamento:
# O encapsulamento é um princípio da orientação a objetos que visa proteger os dados internos de uma classe,
# restringindo o acesso direto a atributos e métodos que não devem ser modificados ou utilizados fora dela.
# 
# No Python, não existem modificadores de acesso como "private" ou "protected". No entanto, há convenções:
# - Um único underscore (_): Indica que o atributo ou método é "privado" e não deve ser acessado diretamente.
# - Dois underscores (__): Ativam o name mangling, renomeando o atributo internamente para evitar acessos acidentais.
#
# Boas práticas:
# - Use métodos públicos (getters e setters) para acessar ou modificar atributos "privados".
# - Respeite as convenções (_ e __) para manter o código claro e seguro.
# 
# Exemplo:
# self._atributo (indica que é privado, mas pode ser acessado com cuidado)
# self.__atributo (é renomeado internamente, dificultando o acesso direto)

    def extrato(self):
        """
        Método para exibir o saldo atual e o titular da conta.

        Este método usa os atributos do objeto para exibir as informações da conta.
        """
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        """
        Método para adicionar um valor ao saldo da conta.

        Args:
        - valor (float): Valor a ser depositado.
        """
        self.__saldo += valor  # Adiciona o valor ao saldo atual
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    def saca(self, valor):
        """
        Método para retirar um valor do saldo da conta.

        Args:
        - valor (float): Valor a ser retirado.
        """
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")  # Subtrai o valor do saldo atual

    def transfere(self, conta_destino, valor):
        self.saca(valor)
        conta_destino.deposita(valor)
        print("{valor} transferido para {conta_destino}".format(conta_destino=conta_destino, valor=valor))

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):            #def get_limite(self):
        """
        Decorator @property:
        - Transforma o método 'limite()' em um getter.
        - Permite acessar 'conta.limite' como se fosse um atributo público.
        - Útil para adicionar lógica ou restrições ao acesso de atributos privados.
        
        Exemplo:
        conta = Conta(1000)
        print(conta.limite)  # Acessa o valor do atributo '__limite' indiretamente.
        """
        return self.__limite

    @limite.setter
    def limite(self, limite):
        """
        Decorator @setter:
        - Usado em conjunto com @property para definir um setter para o atributo privado.
        - Permite alterar 'conta.limite' como se fosse um atributo público.
        - Útil para validações ou modificações antes de atualizar o valor do atributo.
        
        Exemplo:
        conta.limite = 2000  # Atualiza o valor do atributo '__limite' com controle.
        """
        self.__limite = limite
    
    @staticmethod #decorator Metodo estatico
    def codigo_banco():
        """
        Decorator @staticmethod:
        - Define um método que não depende de nenhuma instância ou atributo da classe.
        - Pode ser chamado diretamente pela classe, sem a necessidade de criar um objeto.
        - Não usa o argumento 'self' nem 'cls'.
        
        Exemplo:
        print(Conta.codigo_banco())  # Retorna "001".
        """
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
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