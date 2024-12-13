class Cliente:
    """
    A classe Cliente demonstra o uso de encapsulamento em Python, com a implementação de getters, setters e o decorador @property.
    """
    def __init__(self, nome, idade):
        # Atributos privados (usando __ para aplicar name mangling)
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        """
        O decorador @property transforma o método 'nome()' em um getter. 
        Ele permite acessar o atributo '__nome' como se fosse um atributo público, 
        mas mantendo o controle e a possibilidade de adicionar lógica personalizada.
        
        Exemplo de uso:
        cliente = Cliente("João", 30)
        print(cliente.nome)  # Chamará este método automaticamente.
        """
        print("Chamando @property nome()...")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        """
        O decorador @nome.setter transforma o método 'nome()' em um setter.
        Ele permite modificar o atributo '__nome' com controle adicional, como validações ou transformação de dados.

        Exemplo de uso:
        cliente = Cliente("João", 30)
        cliente.nome = "Maria"  # Chamará este método automaticamente.
        """
        print("Chamando setter nome()...")
        self.__nome = nome
