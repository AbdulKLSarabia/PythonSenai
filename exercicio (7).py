'''Exercício 4: Sistema de Pedidos em um Restaurante
Crie uma classe base Pedido com métodos para adicionar itens ao pedido e calcular o total. Em seguida, crie subclasses para representar diferentes tipos de pedidos, como PedidoOnline e PedidoPresencial. Cada subclasse deve ter métodos específicos, como calcular taxa de entrega para PedidoOnline e aplicar desconto para PedidoPresencial.

DICA: Identifique os Comportamentos Gerais de um Pedido: Comece identificando os comportamentos comuns a todos os tipos de pedidos, como adicionar itens e calcular o total.
Comportamentos Específicos para Cada Tipo de Pedido: Considere os comportamentos específicos para pedidos online e presenciais. Por exemplo, um pedido online pode ter um método para calcular a taxa de entrega, enquanto um pedido presencial pode ter um método para aplicar desconto.
Encapsule as Funcionalidades: Utilize métodos para encapsular as funcionalidades relacionadas a cada tipo de pedido, mantendo o código organizado e de fácil compreensão.
'''

class Pedido:
    def __init__(self):
        self.itens = []  # Lista de itens do pedido

    def adicionar_item(self, item, preco):
        """Adiciona um item ao pedido."""
        self.itens.append((item, preco))

    def calcular_total(self):
        """Calcula o total do pedido."""
        total = sum(preco for _, preco in self.itens)
        return total

class PedidoOnline(Pedido):
    def __init__(self, taxa_entrega):
        super().__init__()
        self.taxa_entrega = taxa_entrega

    def calcular_total(self):
        """Calcula o total do pedido online, incluindo a taxa de entrega."""
        total_pedido = super().calcular_total()
        total_com_taxa = total_pedido + self.taxa_entrega
        return total_com_taxa

class PedidoPresencial(Pedido):
    def __init__(self, desconto):
        super().__init__()
        self.desconto = desconto

    def calcular_total(self):
        """Calcula o total do pedido presencial, aplicando o desconto."""
        total_pedido = super().calcular_total()
        total_com_desconto = total_pedido * (1 - self.desconto)
        return total_com_desconto

# Exemplo de uso:
pedido_online = PedidoOnline(taxa_entrega=5)
pedido_online.adicionar_item("Pizza", 30)
pedido_online.adicionar_item("Refrigerante", 5)
total_online = pedido_online.calcular_total()
print(f"Total do pedido online: R${total_online:.2f}")

pedido_presencial = PedidoPresencial(desconto=0.1)  # 10% de desconto
pedido_presencial.adicionar_item("Hambúrguer", 20)
pedido_presencial.adicionar_item("Batata frita", 10)
total_presencial = pedido_presencial.calcular_total()
print(f"Total do pedido presencial: R${total_presencial:.2f}")
