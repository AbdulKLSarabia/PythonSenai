"""Exercício 2: Herança em Animais
Crie uma classe base Animal com métodos comuns a todos os animais, como comer e dormir. Em seguida, crie subclasses para representar diferentes tipos de animais, como Mamífero, Réptil e Ave. Cada subclasse deve ter seus próprios métodos e atributos específicos.

DICA: Abstração dos Comportamentos: Identifique os comportamentos comuns a todos os animais, como comer, dormir e se locomover.
Diferenças entre os Tipos de Animais: Considere as diferenças entre mamíferos, répteis e aves. Pense em características específicas de cada grupo que podem ser representadas como atributos ou métodos em suas respectivas subclasses.
Reutilize Código: Utilize a herança para compartilhar comportamentos comuns entre as classes, evitando repetição de código.
"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

    def locomover(self):
        print(f"{self.nome} está se locomovendo.")

class Mamifero(Animal):
    def __init__(self, nome, pelos, gestacao):
        super().__init__(nome)
        self.pelos = pelos
        self.gestacao = gestacao

    def amamentar(self):
        print(f"{self.nome} está amamentando.")

    def correr(self):
        print(f"{self.nome} está correndo.")

class Reptil(Animal):
    def __init__(self, nome, escamas):
        super().__init__(nome)
        self.escamas = escamas

    def rastejar(self):
        print(f"{self.nome} está rastejando.")

    def botar_ovos(self):
        print(f"{self.nome} está botando ovos.")

class Ave(Animal):
    def __init__(self, nome, penas):
        super().__init__(nome)
        self.penas = penas

    def voar(self):
        print(f"{self.nome} está voando.")

    def construir_ninhos(self):
        print(f"{self.nome} está construindo um ninho.")

# Exemplo de uso:
gato = Mamifero("Gato", True, True)
gato.comer()
gato.correr()

cobra = Reptil("Cobra", True)
cobra.locomover()
cobra.botar_ovos()

pombo = Ave("Pombo", True)
pombo.dormir()
pombo.construir_ninhos()
