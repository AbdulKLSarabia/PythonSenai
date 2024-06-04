produtos_disponiveis = [
    {"id": 1, "nome": "Arroz", "preco": 29.99},
    {"id": 2, "nome": "Feijão", "preco": 19.99},
    {"id": 3, "nome": "Macarrão", "preco": 15.99},
    {"id": 4, "nome": "Leite", "preco": 4.99},
    {"id": 5, "nome": "Carne", "preco": 44.99},
    {"id": 6, "nome": "Ovo", "preco": 14.99},
    {"id": 7, "nome": "Pão", "preco": 4.99},
    {"id": 8, "nome": "Banana", "preco": 4.99},
    {"id": 9, "nome": "Café", "preco": 6.99},
    {"id": 10, "nome": "Queijo", "preco": 15.99},
]

carrinho = {}

def listar_produtos():
    print("Produtos disponíveis:")
    for produto in produtos_disponiveis:
        print(f"{produto['id']}: {produto['nome']} - R${produto['preco']:.2f}")
    print()

def adicionar_ao_carrinho(produto_id, quantidade=1):
    produto = next((p for p in produtos_disponiveis if p['id'] == produto_id), None)
    if produto:
        if produto_id in carrinho:
            carrinho[produto_id] += quantidade
        else:
            carrinho[produto_id] = quantidade
        print(f"{quantidade} unidades de {produto['nome']} adicionadas ao carrinho.")
    else:
        print(f"Produto com ID {produto_id} não encontrado.")
    print()

def visualizar_carrinho():
    print("Carrinho de compras:")
    for produto_id, quantidade in carrinho.items():
        produto = next((p for p in produtos_disponiveis if p['id'] == produto_id), None)
        if produto:
            print(f"{produto['nome']} ({quantidade} unidades) - R${produto['preco'] * quantidade:.2f}")
    print()

def finalizar_compra():
    total = sum(produtos_disponiveis[produto_id - 1]['preco'] * quantidade for produto_id, quantidade in carrinho.items())
    print(f"Total da compra: R${total:.2f}")



# Exemplo de uso:
listar_produtos()
adicionar_ao_carrinho(1, 2)
adicionar_ao_carrinho(4, 5)
adicionar_ao_carrinho(5, 4)
visualizar_carrinho()
finalizar_compra()
print()