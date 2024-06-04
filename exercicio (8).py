'''Exercício 5: Sistema Bancário Simples
Crie uma classe ContaBancaria com métodos para depositar, sacar e verificar saldo. Em seguida, crie subclasses para representar diferentes tipos de contas, como ContaCorrente e ContaPoupanca. Adicione métodos específicos a cada subclasse, como cobrar tarifa de manutenção para ContaCorrente e calcular juros para ContaPoupanca.

DICA:Identifique as Operações Bancárias Básicas: Comece identificando as operações básicas que podem ser realizadas em qualquer tipo de conta bancária, como depositar, sacar e verificar saldo.
Comportamentos Específicos de Cada Tipo de Conta: Considere os comportamentos específicos para contas correntes e poupanças. Por exemplo, uma conta corrente pode ter um método para cobrar tarifa de manutenção, enquanto uma conta poupança pode ter um método para calcular juros.
Organize Hierarquicamente as Classes: Utilize a herança para organizar as classes de forma hierárquica, compartilhando comportamentos comuns entre as diferentes tipos de contas.
'''

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        self.saldo += valor

    def sacar(self, valor):
        """Realiza um saque da conta."""
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def verificar_saldo(self):
        """Verifica o saldo atual da conta."""
        print(f"Saldo atual: R${self.saldo:.2f}")

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo_inicial=0, tarifa_manutencao=5):
        super().__init__(saldo_inicial)
        self.tarifa_manutencao = tarifa_manutencao

    def cobrar_tarifa_manutencao(self):
        """Cobra a tarifa de manutenção da conta corrente."""
        self.saldo -= self.tarifa_manutencao

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo_inicial=0, taxa_juros=0.02):
        super().__init__(saldo_inicial)
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        """Calcula os juros da conta poupança."""
        juros = self.saldo * self.taxa_juros
        self.saldo += juros

# Exemplo de uso:
conta_corrente = ContaCorrente(saldo_inicial=100)
conta_corrente.depositar(50)
conta_corrente.cobrar_tarifa_manutencao()
conta_corrente.verificar_saldo()

conta_poupanca = ContaPoupanca(saldo_inicial=500)
conta_poupanca.depositar(100)
conta_poupanca.calcular_juros()
conta_poupanca.verificar_saldo()
