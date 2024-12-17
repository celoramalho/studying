class Colaborador:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario
    
    @property
    def nome(self):
        return self._nome
    
    def funcao(self):
        print(f'{self._nome} trabalha...')

class Developer(Colaborador):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def funcao(self):
        print(f'{self._nome} trabalha com programação')

    def mostrar_linguagem(self):
        print(f'{self._nome} programa em Python')

class Gestor(Colaborador):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.__tamanho_equipe = 20

    def funcao(self):
        print(f'{self._nome} gerencia o departamento')

    def cultura_gestao(self):
        print(f'{self._nome} trabalha sempre com foco em pessoas, honestidade, leveza e transparencia')
    
    @property
    def tamanho_equipe(self):
        return self.__tamanho_equipe
    
class TechLead(Developer, Gestor): #a ordem importa 
    pass

rafael_solli = TechLead('Rafael Solli', 20000) 
# TechLead > Developer > Colaborador > Gestor > Colaborador 
#explain Good Head concept TechLead > Developer > Gestor > Colaborador thats how python3 works

rafael_solli.funcao()
rafael_solli.mostrar_linguagem()
rafael_solli.cultura_gestao()
print(f'{rafael_solli.nome} gerencia uma equipe de 20 pessoas')