"""Exercício 1: Hierarquia de Veículos
Crie uma hierarquia de classes para representar diferentes tipos de veículos, como Carro, Moto e Bicicleta. Cada classe deve ter atributos e métodos específicos. Por exemplo, o Carro pode ter um atributo para o número de portas e um método para ligar o motor.
DICA: Identifique os Atributos Comuns: Comece identificando os atributos comuns a todos os tipos de veículos, como marca, modelo e ano.
Pense em Comportamentos Específicos: Considere quais comportamentos são específicos para cada tipo de veículo. Por exemplo, um carro pode ter um método para ligar o motor, enquanto uma bicicleta pode ter um método para pedalar.
Utilize a Herança de Forma Adequada: Use a herança para evitar a duplicação de código. Identifique as semelhanças entre os diferentes tipos de veículos e crie uma classe base que contenha essas características comuns.
"""
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    def ligar_motor(self):
        print("Motor ligado!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_motor = tipo_motor

    def acelerar(self):
        print("Acelerando!")

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, num_marchas):
        super().__init__(marca, modelo, ano)
        self.num_marchas = num_marchas

    def pedalar(self):
        print("Pedalando!")

# Exemplo de uso:
carro1 = Carro("Toyota", "Corolla", 2022, 4)
carro1.ligar_motor()

moto1 = Moto("Honda", "CBR", 2021, "4 tempos")
moto1.acelerar()

bicicleta1 = Bicicleta("Caloi", "Mountain Bike", 2020, 21)
bicicleta1.pedalar()
