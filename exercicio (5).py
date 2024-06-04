'''Exercício 3: Sistema de Cadastro de Pessoas
Crie uma classe Pessoa com atributos como nome, idade e gênero. Em seguida, crie subclasses para representar diferentes tipos de pessoas, como Estudante e Professor. Adicione métodos específicos a cada subclasse, como calcular média para Estudante e listar disciplinas para Professor.
DICA: Identifique os Atributos Comuns: Determine quais atributos são comuns a todos os tipos de pessoas, como nome, idade e gênero.

Comportamentos Específicos: Considere os comportamentos específicos de cada tipo de pessoa. Por exemplo, um estudante pode ter métodos para calcular média e listar disciplinas, enquanto um professor pode ter métodos para adicionar disciplinas e calcular salário.
Organize as Relações: Utilize a herança para representar a relação entre as classes de forma apropriada. Por exemplo, um estudante é um tipo de pessoa, então a classe Estudante pode herdar da classe Pessoa.
'''

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

class Estudante(Pessoa):
    def __init__(self, nome, idade, genero, disciplinas):
        super().__init__(nome, idade, genero)
        self.disciplinas = disciplinas

    def calcular_media(self, notas):
        """Calcula a média das notas do estudante."""
        if notas:
            return sum(notas) / len(notas)
        else:
            return 0.0

    def listar_disciplinas(self):
        print(f"Disciplinas do estudante {self.nome}: {', '.join(self.disciplinas)}")

class Professor(Pessoa):
    def __init__(self, nome, idade, genero, salario):
        super().__init__(nome, idade, genero)
        self.salario = salario

    def adicionar_disciplina(self, disciplina):
        # Implemente a lógica para adicionar uma disciplina ao professor
        pass

    def calcular_salario(self):
        """Calcula o salário do professor (exemplo simplificado)."""
        return self.salario

# Exemplo de uso:
notas_alice = [8.5, 9.0, 7.5]
estudante1 = Estudante("Alice", 20, "Feminino", ["Matemática", "História"])
estudante1.listar_disciplinas()
print(f"Média de notas de {estudante1.nome}: {estudante1.calcular_media(notas_alice):.2f}")

professor1 = Professor("Carlos", 40, "Masculino", 5000)
professor1.adicionar_disciplina("Física")
print(f"Salário do professor {professor1.nome}: R${professor1.calcular_salario():.2f}")

